# Python WiFi Manager 🌐🐍

**A cross-platform WiFi management utility** that simplifies network operations with powerful automation and diagnostics capabilities.

## ✨ Key Features

### 🔌 Connection Management
- **One-click connections** to saved networks
- **Priority-based auto-connect** to preferred networks
- **Batch operations** for multiple networks

### 📊 Network Analysis
```python
# Example: Scan available networks
from wifi_manager import Scanner
scanner = Scanner()
networks = scanner.get_available_ssids()
