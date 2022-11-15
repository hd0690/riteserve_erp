## Riteserve ERP

Riteserve ERP

### Installation steps:

1. Get this app:

    `bench get-app https://github.com/hd0690/riteserve_erp.git`

1. Install this app:

    `bench --site [site-name] install-app riteserve_erp`

1. Migrate changes:

    `bench migrate && bench restart`

1. Download CSV file. [Click here](./data/Leed%20-%20Leed.csv).

1. Now, go to "Data Import" and select Document Type as "Leed" and save.

1. Now, upload the downloaded CSV file and start import.


### Generate PDF of the data:

- Goto "Leed List" and change the "List View" to "Report View" from top-right

- Now, from the left sidebar, select report > "Leed - Report View"

- Now, from the "Menu" (3 dots on top right), select "Print".

- You'll be able to see the report as PDF.

### Reports:

1. Number of Leads signed till September 2022
1. Lead Signed Till September 2022
1. Lead Status Report
1. Lead Stage Report
1. Forecast Revenue
1. Potential Lost Revenue


#### License

MIT