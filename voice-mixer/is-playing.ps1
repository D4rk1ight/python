$DeviceMaster = Get-AudioDevice - List

if ($DeviceMaster.GetPeakValue() -gt 0) {
  echo "Звук играет"
} else {
  echo "Звук не играет"
}
