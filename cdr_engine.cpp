#ifndef _WIN32_WINNT
#define _WIN32_WINNT 0x0A00
#endif
#include <stddef.h>
#include <string.h>
#include <windows.h>
#include <winreg.h>
// PSAPI_VERSION 1 ensures K32EnumProcesses and K32EmptyWorkingSet are available
#ifndef PSAPI_VERSION
#define PSAPI_VERSION 1
#endif
#include <psapi.h>
#pragma comment(lib, "psapi.lib")

#ifndef REG_OPTION_NON_VOLATILE
#define REG_OPTION_NON_VOLATILE 0
#endif
#ifndef KEY_WRITE
#define KEY_WRITE 0x20006
#endif
#ifndef KEY_WOW64_64KEY
#define KEY_WOW64_64KEY 0x0100
#endif
#ifndef REG_DWORD
#define REG_DWORD 4
#endif
#ifndef REG_SZ
#define REG_SZ 1
#endif
#ifndef HKEY_LOCAL_MACHINE
#define HKEY_LOCAL_MACHINE ((HKEY)(ULONG_PTR)((LONG)0x80000002))
#endif

typedef long NTSTATUS;
#ifndef STATUS_SUCCESS
#define STATUS_SUCCESS ((NTSTATUS)0)
#endif

#ifndef LSTATUS
typedef long LSTATUS;
#endif

extern "C" {

__declspec(dllexport) int OptimizeMemory_CPP() {
  DWORD aProcesses[2048], cbNeeded, cProcesses;
  if (!K32EnumProcesses(aProcesses, sizeof(aProcesses), &cbNeeded)) {
    return 0;
  }

  cProcesses = (DWORD)(cbNeeded / sizeof(DWORD));
  int optimizedCount = 0;

  for (DWORD i = 0; i < cProcesses; i++) {
    if (aProcesses[i] != 0) {
      HANDLE hProcess = OpenProcess(
          PROCESS_QUERY_INFORMATION | PROCESS_SET_QUOTA, FALSE, aProcesses[i]);
      if (hProcess != NULL) {
        if (K32EmptyWorkingSet(hProcess)) {
          optimizedCount++;
        } else {
          SetProcessWorkingSetSize(hProcess, (SIZE_T)-1, (SIZE_T)-1);
          optimizedCount++;
        }
        CloseHandle(hProcess);
      }
    }
  }
  return optimizedCount;
}

__declspec(dllexport) int
ApplyRegistryDWORD_CPP(const char *subkey, const char *valueName, DWORD data) {
  HKEY hKey;
  LSTATUS status = RegCreateKeyExA(
      HKEY_LOCAL_MACHINE, subkey, 0, NULL, REG_OPTION_NON_VOLATILE,
      KEY_WRITE | KEY_WOW64_64KEY, NULL, &hKey, NULL);
  if (status == ERROR_SUCCESS) {
    status = RegSetValueExA(hKey, valueName, 0, REG_DWORD, (const BYTE *)&data,
                            sizeof(data));
    RegCloseKey(hKey);
    return (status == ERROR_SUCCESS) ? 1 : 0;
  }
  return 0;
}

__declspec(dllexport) int ApplyRegistryString_CPP(const char *subkey,
                                                  const char *valueName,
                                                  const char *data) {
  HKEY hKey;
  LSTATUS status = RegCreateKeyExA(
      HKEY_LOCAL_MACHINE, subkey, 0, NULL, REG_OPTION_NON_VOLATILE,
      KEY_WRITE | KEY_WOW64_64KEY, NULL, &hKey, NULL);
  if (status == ERROR_SUCCESS) {
    status = RegSetValueExA(hKey, valueName, 0, REG_SZ, (const BYTE *)data,
                            (DWORD)(strlen(data) + 1));
    RegCloseKey(hKey);
    return (status == ERROR_SUCCESS) ? 1 : 0;
  }
  return 0;
}

__declspec(dllexport) int PingEngine() { return 42; }

__declspec(dllexport) int FlushStandbyList_CPP() {
  typedef enum _SYSTEM_INFORMATION_CLASS {
    SystemMemoryListInformation = 80
  } SYSTEM_INFORMATION_CLASS;

  typedef enum _MEMORY_LIST_COMMAND {
    MemoryPurgeStandbyList = 11
  } MEMORY_LIST_COMMAND;

  typedef NTSTATUS(WINAPI * pNtSetSystemInformation)(INT, PVOID, ULONG);

  HMODULE ntdll = GetModuleHandleA("ntdll.dll");
  if (!ntdll)
    return 0;

  pNtSetSystemInformation NtSetSystemInformation =
      (pNtSetSystemInformation)GetProcAddress(ntdll, "NtSetSystemInformation");
  if (!NtSetSystemInformation)
    return 0;

  MEMORY_LIST_COMMAND command = MemoryPurgeStandbyList;
  NTSTATUS status = NtSetSystemInformation(SystemMemoryListInformation,
                                           &command, sizeof(command));

  return (status == 0) ? 1 : 0;
}

__declspec(dllexport) int SetHighPriority_CPP(DWORD dwProcessId) {
  HANDLE hProcess = OpenProcess(PROCESS_SET_INFORMATION, FALSE, dwProcessId);
  if (hProcess == NULL)
    return 0;

  BOOL success = SetPriorityClass(hProcess, HIGH_PRIORITY_CLASS);
  CloseHandle(hProcess);

  return success ? 1 : 0;
}

// ─── HKCU Registry Write (for current user keys, no WOW64 redirection) ───────
__declspec(dllexport) int
ApplyRegistryCU_DWORD(const char *subkey, const char *valueName, DWORD data) {
  HKEY hKey;
  LSTATUS status =
      RegCreateKeyExA(HKEY_CURRENT_USER, subkey, 0, NULL,
                      REG_OPTION_NON_VOLATILE, KEY_WRITE, NULL, &hKey, NULL);
  if (status == ERROR_SUCCESS) {
    status = RegSetValueExA(hKey, valueName, 0, REG_DWORD, (const BYTE *)&data,
                            sizeof(data));
    RegCloseKey(hKey);
    return (status == ERROR_SUCCESS) ? 1 : 0;
  }
  return 0;
}

__declspec(dllexport) int ApplyRegistryCU_String(const char *subkey,
                                                 const char *valueName,
                                                 const char *data) {
  HKEY hKey;
  LSTATUS status =
      RegCreateKeyExA(HKEY_CURRENT_USER, subkey, 0, NULL,
                      REG_OPTION_NON_VOLATILE, KEY_WRITE, NULL, &hKey, NULL);
  if (status == ERROR_SUCCESS) {
    status = RegSetValueExA(hKey, valueName, 0, REG_SZ, (const BYTE *)data,
                            (DWORD)(strlen(data) + 1));
    RegCloseKey(hKey);
    return (status == ERROR_SUCCESS) ? 1 : 0;
  }
  return 0;
}

// ─── Service Control via WinAPI (NO subprocess / no sc.exe spawn)
// ─────────────
__declspec(dllexport) int DisableService(const char *serviceName) {
  SC_HANDLE hSCM = OpenSCManagerA(NULL, NULL, SC_MANAGER_ALL_ACCESS);
  if (!hSCM)
    return 0;

  SC_HANDLE hSvc =
      OpenServiceA(hSCM, serviceName,
                   SERVICE_STOP | SERVICE_CHANGE_CONFIG | SERVICE_QUERY_STATUS);
  int result = 0;
  if (hSvc) {
    // Try to stop the service first
    SERVICE_STATUS ss;
    ControlService(hSvc, SERVICE_CONTROL_STOP, &ss);
    // Disable it (set start type to DISABLED)
    if (ChangeServiceConfigA(hSvc, SERVICE_NO_CHANGE, SERVICE_DISABLED,
                             SERVICE_NO_CHANGE, NULL, NULL, NULL, NULL, NULL,
                             NULL, NULL)) {
      result = 1;
    }
    CloseServiceHandle(hSvc);
  }
  CloseServiceHandle(hSCM);
  return result;
}

// ─── Batch service disabler: semicolon-separated list
// ───────────────────────── Example:
// BatchDisableServices("DiagTrack;SysMain;WSearch;XblGameSave") Returns number
// of successfully disabled services
__declspec(dllexport) int BatchDisableServices(const char *serviceList) {
  if (!serviceList || !*serviceList)
    return 0;

  SC_HANDLE hSCM = OpenSCManagerA(NULL, NULL, SC_MANAGER_ALL_ACCESS);
  if (!hSCM)
    return 0;

  char buf[4096];
  strncpy(buf, serviceList, sizeof(buf) - 1);
  buf[sizeof(buf) - 1] = '\0';

  int count = 0;
  char *ctx = NULL;
  char *tok = strtok_s(buf, ";", &ctx);
  while (tok) {
    // Trim leading spaces
    while (*tok == ' ')
      tok++;
    if (*tok) {
      SC_HANDLE hSvc = OpenServiceA(hSCM, tok,
                                    SERVICE_STOP | SERVICE_CHANGE_CONFIG |
                                        SERVICE_QUERY_STATUS);
      if (hSvc) {
        SERVICE_STATUS ss;
        ControlService(hSvc, SERVICE_CONTROL_STOP, &ss);
        if (ChangeServiceConfigA(hSvc, SERVICE_NO_CHANGE, SERVICE_DISABLED,
                                 SERVICE_NO_CHANGE, NULL, NULL, NULL, NULL,
                                 NULL, NULL, NULL)) {
          count++;
        }
        CloseServiceHandle(hSvc);
      }
    }
    tok = strtok_s(NULL, ";", &ctx);
  }
  CloseServiceHandle(hSCM);
  return count;
}

// ─── Run a command hidden (for legacy fallback cases)
// ─────────────────────────
__declspec(dllexport) int RunHidden(const char *cmd) {
  STARTUPINFOA si = {sizeof(si)};
  si.dwFlags = STARTF_USESHOWWINDOW;
  si.wShowWindow = SW_HIDE;
  PROCESS_INFORMATION pi = {};
  char cmdBuf[2048];
  strncpy(cmdBuf, cmd, sizeof(cmdBuf) - 1);
  BOOL ok = CreateProcessA(NULL, cmdBuf, NULL, NULL, FALSE, CREATE_NO_WINDOW,
                           NULL, NULL, &si, &pi);
  if (ok) {
    WaitForSingleObject(pi.hProcess, 30000);
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);
    return 1;
  }
  return 0;
}
}
