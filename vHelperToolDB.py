import winreg


class RegKey:
    def __init__(self, handle, path, name, registry_type, defaultvalue=None, description=None, kb=None):
        self.handle = handle
        self.path = path
        self.name = name
        self.registry_type = registry_type
        self.description = description
        self.defaultvalue = defaultvalue
        self.kb = kb

    def get_reg(self):
        try:
            registry_key = winreg.OpenKey(self.handle, self.path)
            value, keyname = winreg.QueryValueEx(registry_key, self.name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None

    def set_reg(self, key_value):
        try:
            winreg.CreateKey(self.handle, self.path)
            registry_key = winreg.OpenKey(self.handle, self.path, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(registry_key, self.name, 0, self.registry_type, key_value)
            winreg.CloseKey(registry_key)
        except WindowsError:
            pass

    def reset_reg(self):
        try:
            winreg.CreateKey(self.handle, self.path)
            registry_key = winreg.OpenKey(self.handle, self.path, 0, winreg.KEY_ALL_ACCESS)
            winreg.SetValueEx(registry_key, self.name, 0, self.registry_type, self.defaultvalue)
            winreg.CloseKey(registry_key)
        except WindowsError:
            pass

    def deletevalue_reg(self):
        try:
            winreg.CreateKey(self.handle, self.path)
            registry_key = winreg.OpenKey(self.handle, self.path, 0, winreg.KEY_ALL_ACCESS)
            winreg.DeleteValue(registry_key, self.name)
            winreg.CloseKey(registry_key)
        except WindowsError:
            pass


HKLM = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
HKCU = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)

BackupCopyLookForward = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"BackupCopyLookForward", winreg.REG_DWORD, 1, r"If you do not want backup copy jobs to transfer the latest point after each restart, set this to 1 to only look for restore points newer than the start time", r"None")
BlockSnapshotThreshold = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"BlockSnapshotThreshold", winreg.REG_DWORD, 2, r"Veeam Backup & Replication warns you when there is not enough space for snapshots", r"None")
BodyPayloadCompressionDisabled = RegKey(HKLM, r"SOFTWARE\Wow6432Node\Veeam\Veeam Backup Transport", r"BodyPayloadCompressionDisabled", winreg.REG_DWORD, 1, r"Disable the Body Payload Compression verification for speed performance. Set to 1 to disable the verification process", r"None")
CatalogPath = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup Catalog", r"CatalogPath", winreg.REG_SZ, r"C:\VBRCatalog\ ", r"Change the path to change the Veeam Backup Catalog Folder. Follow steps as described in KB1453", r"None")
CloudReplicaNoStaticIpSDetectedWarning = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"CloudReplicaNoStaticIpSDetectedWarning", winreg.REG_DWORD, 0, r"Supresses irrelevant warnings caused by above registry keys when backing up a non-Windows VM. Set to 0 and restart Veeam Backup Service will disable the warning", r"None")
ConnectByIPsTimeoutSec = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"ConnectByIPsTimeoutSec", winreg.REG_DWORD, 1200, r"Increase/set IP connection timeout for when jobs that are using a proxy, windows repository, or Hyper-V host that have multiple NICs are failing with \"Error: Completion Timeout Occurred\"", r"kb1976")
CorePath = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"CorePath", winreg.REG_SZ, r"C:\Program Files\Veeam\Backup and Replication\Backup\ ", r"Registry Key which point to the installation folder of the Veeam Backup Validator", r"kb2086")
CutHvVmSecuritySettings = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"CutHvVmSecuritySettings", winreg.REG_DWORD, 1, r"See KB2021 for details", r"None")
DataMoverLocalFastPath = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"DataMoverLocalFastPath", winreg.REG_DWORD, 2, r"Alter the behaviour of the Veeam Data mover communication when both are running on the same server: 0) No optization (not advised) 1)TCP Loopback (slower) 2) Shared Momory (default and fastest)", r"None")
DefaultCASServer = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"DefaultCASServer", winreg.REG_DWORD, 1, r"Ability to force CAS server for Veeam Explorer for Microsoft Exchange (instead of automatically detecting one)", r"kb2147")
DisablePublicIPTrafficEncryption = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"DisablePublicIPTrafficEncryption", winreg.REG_DWORD, 1, r"(SAFETY WARNING!) Veeam Backup & Replication enables encryption when a server and agent is run on has a Public IP. This is intended as a safety feature however the overhead of encryption can diminish performance. Set to 1 to disable encryption. ", r"kb2055")
DisableVBKRename = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"DisableVBKRename", winreg.REG_DWORD, 1, r"Prevent the .VBK file from being renamed. Set to 1, to enable. Note: This function only works with Backup Jobs using Reversed Incremental. ", r"kb1076")
EnableHvVDK = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"EnableHvVDK", winreg.REG_DWORD, 1, r"By default, the Veeam VDK driver is used to mount VM disks for file level restore. To use the native Hyper-V disk mount driver instead, set this value to 0.", r"None")
EnableRestoreSNMPTraps = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"EnableRestoreSNMPTraps", winreg.REG_DWORD, 1, r"Trigger snmp traps for both Windows and Multi-OS File-Level Recovery. Set to 1 to enable", r"kb2024")
ForceDeleteBackupFiles = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"ForceDeleteBackupFiles", winreg.REG_DWORD, 3, r"Please read the KB for details on: How to configure Veeam for rotated media", r"kb1154")
HashRepositoryBasePath = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"HashRepositoryBasePath", winreg.REG_SZ, None, r"When deploying a new Wan Accelerator in the Backup Infrastructur, an error msg appears Installing package VeeamWANSvc_x64.msi Error: Error 1920. Service Veeam WAN Accelerator Service (VeeamWANSvc) failed to start. Verify that you have sufficient privileges to start system services. Manual installation also fails. This is becaus the ervice installer is pointing to an invalid path in the Registry on the server. This occurs most often when the role is removed from the server, then the original drive used for the WAN Accelerator cache was removed. Manaually point these registry items to the same valid directory path: HashRepositoryBasePath, HashRepository and GlobalDedupBasePath.", r"kb1828")
HashRepositoryGlobalDedupBasePath = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"HashRepositoryGlobalDedupBasePath", winreg.REG_SZ, None, r"When deploying a new Wan Accelerator in the Backup Infrastructur, an error msg appears Installing package VeeamWANSvc_x64.msi Error: Error 1920. Service Veeam WAN Accelerator Service (VeeamWANSvc) failed to start. Verify that you have sufficient privileges to start system services. Manual installation also fails. This is becaus the ervice installer is pointing to an invalid path in the Registry on the server. This occurs most often when the role is removed from the server, then the original drive used for the WAN Accelerator cache was removed. Manaually point these registry items to the same valid directory path: HashRepositoryBasePath, HashRepository and GlobalDedupBasePath.", r"kb1828")
HvDelayBeforeSnapshotImportCompleteSec = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"HvDelayBeforeSnapshotImportCompleteSec", winreg.REG_DWORD, 90, r"See KB1844 for details", r"None")
InfrastructureCacheExpirationSec = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"InfrastructureCacheExpirationSec", winreg.REG_DWORD, 900, r"To remove the wait time for virtual infrastructure objects to be loaded, the user interface now uses an infrastructure cache in certain places, such as in the Backup Job wizards and in the Virtual Machines tab.", r"None")
LogDirectory = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"LogDirectory", winreg.REG_SZ, None, r"Set Default log directory location", r"None")
LoggingLevel = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"LoggingLevel", winreg.REG_DWORD, 4, r"Logging level: 6 = UltimateDetailed, 5 = HighDetailed, 4 = AboveNormal (DEFAULT), 3 = Normal, 2 = BelowNormal, 1 = LowDetailed", r"None")
LogsArchivesMaxCount = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"LogsArchivesMaxCount", winreg.REG_DWORD, 10, r"Total amount of archived generations of logs", r"None")
MaxLogCount = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"MaxLogCount", winreg.REG_DWORD, 10, r"Maximum log count. Number of log generations to retain.", r"None")
MaxLogSize = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"MaxLogSize", winreg.REG_DWORD, 10240, r"Maximum log file size in KiB. New files are created when a file reaches the set max size. ", r"None")
MaxPerlSoapOperationTimeout = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"MaxPerlSoapOperationTimeout", winreg.REG_DWORD, 600000, r"Certain operations over SSH to a Linux/Exagrid repository timeout after 100 seconds. Set the timeout value in milliseconds to alter the timeout.", r"kb1176")
MaxVmCountOnHvHardSnapshot = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"MaxVmCountOnHvHardSnapshot", winreg.REG_DWORD, 8, r"For reliability reasons caused by Hyper-V backup architecture, when a hardware VSS provider is used the maximum amount of VMs per snapshot is limited to eight by default. This value can be increased on fast storage, or decreased for troubleshooting purposes.", r"None")
MaxVmCountOnHvSoftSnapshot = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"MaxVmCountOnHvSoftSnapshot", winreg.REG_DWORD, 4, r"For reliability reasons caused by Hyper-V backup architecture, when a software VSS provider is used the maximum amount of VMs per snapshot is limited to four by default. This value can be increased on fast storage, or decreased for troubleshooting purposes.", r"None")
NetUseShareAccess = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"NetUseShareAccess", winreg.REG_DWORD, 1, r"- reboot required - Please read the KB for more details: Allows Data Movers to open backup files by a resilient method similar to the Windows net use command", r"kb1735")
PayloadChecksumsDisabled = RegKey(HKLM, r"SOFTWARE\Wow6432Node\Veeam\Veeam Backup Transport", r"PayloadChecksumsDisabled", winreg.REG_DWORD, 1, r"Disable the Payload Checksum verification for speed performance. Set to 1 to disable the verification process", r"None")
PostJobScriptTimeoutSec = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"PostJobScriptTimeoutSec", winreg.REG_DWORD, 900, r"Execution timeout for scripts run after a job, in seconds", r"None")
PreJobScriptTimeoutSec = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"PreJobScriptTimeoutSec", winreg.REG_DWORD, 900, r"Execution timeout for scripts run before a job, in seconds", r"None")
Remoting_MachineName = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"Remoting_MachineName", winreg.REG_SZ, None, r"Manually sets which FQDN the Veeam Backup Server will send to the Backup Enteprise Manager server. Apply this entry on the Veeam Backup Server. Enterprise Manager must be able to resolve FQDN or HostName though DNS or hosts file.", r"None")
Remoting_UseIPAddress = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"Remoting_UseIPAddress", winreg.REG_SZ, r"true", r"Control whether Veeam Backup & Replication must send its local IP or not (should be set to “false” to allow Veeam Enterprise Manager to connect over NAT). Apply on Veeam Backup Server.", r"kb2098")
SessTimeout = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"SessTimeout", winreg.REG_DWORD, 600, r"- reboot required - Please read the KB for more details: This increases the amount of time the Windows SMB client will wait for a response from an SMB server before it aborts the connection. The default timeout is 60 seconds", r"None")
ShowSplashScreen = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"ShowSplashScreen", winreg.REG_DWORD, 1, r"To hide the splash screen that appears while the console is loading, set this value to 0", r"None")
SshFingerprintCheck = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"SshFingerprintCheck", winreg.REG_DWORD, None, r"Set to XX to disable Storage fingerprint check", r"None")
TcpMaxDataRetransmissions = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"TcpMaxDataRetransmissions", winreg.REG_DWORD, 10, r"- reboot required - Please read the KB for more details: This increases the number of times the Windows TCP implementation will retransmit a data segment before it aborts the connection. The default number of retries is 5", r"None")
UIShowAllVssProvidersForVolume = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"UIShowAllVssProvidersForVolume", winreg.REG_DWORD, 1, r"This value disables the advanced compatibility step which automatically chooses the best compatible providers", r"None")
UncompressedLogsMaxTotalSize = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"UncompressedLogsMaxTotalSize", winreg.REG_DWORD, 512000, r"Total size in KiB of uncompressed logs, applies per job.", r"None")
UseLowBandwithMode = RegKey(HKLM, r"SOFTWARE\Wow6432Node\Veeam\Veeam Backup Transport", r"UseLowBandwithMode", winreg.REG_DWORD, 1, r"If the Catalyst Store is configured as High Bandwidth on the appliance, Low Bandwidth mode can be forced by setting it to 1", r"None")
VSSGuestSnapshotTimeout = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"VSSGuestSnapshotTimeout", winreg.REG_DWORD, 1200, r"Change the timout for a VSS Snapshot (in seconds)", r"None")
WanRootCachePath = RegKey(HKLM, r"SOFTWARE\Veeam\Veeam Backup and Replication", r"WanRootCachePath", winreg.REG_SZ, None, r"When deploying a new Wan Accelerator in the Backup Infrastructur, an error msg appears Installing package VeeamWANSvc_x64.msi Error: Error 1920. Service Veeam WAN Accelerator Service (VeeamWANSvc) failed to start. Verify that you have sufficient privileges to start system services. Manual installation also fails. This is becaus the ervice installer is pointing to an invalid path in the Registry on the server. This occurs most often when the role is removed from the server, then the original drive used for the WAN Accelerator cache was removed. Manaually point these registry items to the same valid directory path: HashRepositoryBasePath, HashRepository and GlobalDedupBasePath.", r"kb1828")


RegKeyList = [
    BackupCopyLookForward,
    BlockSnapshotThreshold,
    BodyPayloadCompressionDisabled,
    CatalogPath,
    CloudReplicaNoStaticIpSDetectedWarning,
    ConnectByIPsTimeoutSec,
    CorePath,
    CutHvVmSecuritySettings,
    DataMoverLocalFastPath,
    DefaultCASServer,
    DisablePublicIPTrafficEncryption,
    DisableVBKRename,
    EnableHvVDK,
    EnableRestoreSNMPTraps,
    ForceDeleteBackupFiles,
    HashRepositoryBasePath,
    HashRepositoryGlobalDedupBasePath,
    HvDelayBeforeSnapshotImportCompleteSec,
    InfrastructureCacheExpirationSec,
    LogDirectory,
    LoggingLevel,
    LogsArchivesMaxCount,
    MaxLogCount,
    MaxLogSize,
    MaxPerlSoapOperationTimeout,
    MaxVmCountOnHvHardSnapshot,
    MaxVmCountOnHvSoftSnapshot,
    NetUseShareAccess,
    PayloadChecksumsDisabled,
    PostJobScriptTimeoutSec,
    PreJobScriptTimeoutSec,
    Remoting_MachineName,
    Remoting_UseIPAddress,
    SessTimeout,
    ShowSplashScreen,
    SshFingerprintCheck,
    TcpMaxDataRetransmissions,
    UIShowAllVssProvidersForVolume,
    UncompressedLogsMaxTotalSize,
    UseLowBandwithMode,
    VSSGuestSnapshotTimeout,
    WanRootCachePath]

