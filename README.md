
---

# 💱 Odoo 18 Currency Rate Updater – APILayer Integration

This module provides **automated currency exchange rate updates** in Odoo 18 using [APILayer](https://apilayer.com)'s exchange rate API. It extends Odoo’s base currency mechanisms with a configurable backend integration that ensures up-to-date rates for multi-currency transactions.

---

## 📦 Features

- 🔧 Custom currency provider integration via APILayer.
- 🔁 Scheduled auto-update of exchange rates.
- 🧠 Graceful error handling for API requests and connectivity issues.
- 🔐 Secure API key configuration via system settings.
- 🖥️ Admin interface under General Settings for provider management.

---

## 🛠️ Installation

1. Clone the repository into your custom addons folder:
   ```bash
   git clone https://github.com/davidguigui29/currency_rate_update_custom.git
   ```

2. Add the module path to your Odoo configuration (`addons_path`).

3. Restart your Odoo server:
   ```bash
   ./odoo-bin -u currency_rate_update_custom -d your_db_name
   ```

4. Activate Developer Mode in Odoo and navigate to **Settings > General Settings > API Layer Settings**.

---

## ⚙️ Configuration

1. Go to **Settings > General Settings**.
2. Locate the **API Layer Settings** section.
3. Fill in your APILayer API Key.
4. Choose the update frequency from the scheduler settings.

You’re set! Your currency rates will now auto-update based on APILayer’s data.

---

## 🚀 Usage

- Currencies will automatically sync during scheduled cron jobs.
- You can also manually trigger a rate update by navigating to:
  **Invoicing > Configuration > Currency Rates Providers**, 
  - click **New**,
  - Select **APILayer Exchange Rates**,
  - Select from the **Currencies** all currencies you want to update,
  -  and clicking **Update Rates Now**
---

## 📋 TODO

Here are some features planned for future releases:

- [ ] 📊 Dashboard widget to show last update timestamp and source health.
- [ ] 🌍 Support for multiple currency sources (fallback & comparisons).
- [ ] 📆 Custom update intervals per currency.
- [ ] 🔔 Admin alerts for failed updates or API quota issues.
- [ ] 🧪 Unit tests and integration test coverage.
- [ ] 💾 Caching mechanism to avoid redundant API calls.
- [ ] 🌐 Multi-company support and isolation.
- [ ] 🗃️ Historical exchange rate logging and reporting.

---

## 📢 Contributing

We welcome contributions! Please open an issue for bug reports or feature requests, or submit a pull request for improvements.

---

## 🧾 License

This module is released under the [GPL-3 License](https://www.odoo.com/documentation/18.0/legal/licenses/licenses.html#odoo-apps).

---
