# Data-Engineering (Coursera IBM Data Engineering Course)

Project Overview
Scenario
For this project, you will assume the role of data engineer working for an international financial analysis company. Your company tracks stock prices, commodities, forex rates, inflation rates.  Your job is to extract financial data from various sources like websites, APIs and files provided by various financial analysis firms. After you collect the data, you extract the data of interest to your company and transform it based on the requirements given to you. Once the transformation is complete you load that data into a database.

Project Tasks
In this project you will:

Collect data using APIs

Collect data using webscraping.

Download files to process.    

Read csv, xml and json file types.

Extract data from the above file types.

Transform data.

Use the built in logging module.

Save the transformed data in a ready-to-load format which data engineers can use to load the data.

![11](https://github.com/andysingal/Data-Engineering/blob/main/Images/Screenshot%202023-07-11%20at%206.53.42%20PM.png)

![12](https://github.com/andysingal/Data-Engineering/blob/main/Images/Screenshot%202023-07-17%20at%201.36.47%20PM.png)


The following are some considerations for choosing data technologies across the data engineering lifecycle:

- Team size and capabilities: Take an inventory of your team’s skills. Do people lean toward low-code tools, or do they favor code-first approaches? Are people strong in certain languages like Java, Python, or Go? Technologies are available to cater to every preference on the low-code to code-heavy spectrum. 

- Speed to market: Speed to market is crucial in technology. Choose the right technologies, deliver value early, and iterate for continuous improvement. Avoid overthinking and prioritize familiar tools for efficiency. Slow decisions and output can lead to failure; aim for rapid, reliable, and secure operations to succeed.

- Interoperability: Interoperability is crucial when choosing technologies, as they often need to connect and exchange information. Seamlessly integrating products ensures easy setup, while manual configurations may require more effort. Data tools usually have built-in integrations with popular platforms, and standards like JDBC or ODBC enable easy database connections. REST APIs vary, requiring careful integration by vendors or open-source projects. Designing for modularity allows flexibility in swapping technologies as new practices emerge, so consider ease of connecting technologies throughout the data engineering lifecycle. Prioritize interoperability to ensure efficient and effective technology interactions.

- Cost optimization and business value: Interoperability is essential; technologies should connect and exchange information efficiently.
Consider costs through total cost of ownership (TCO) and differentiate between capital expenses (capex) and operational expenses (opex).
Opex allows flexibility and cost-effectiveness, especially in cloud-based services, promoting an opex-first approach.
Total opportunity cost of ownership (TOCO) should be evaluated, as choices may exclude other possibilities and hinder future adaptability.
FinOps focuses on financial accountability, enabling quick iterations and dynamic scalability, ultimately driving business value in data engineering.

- Today versus the future: immutable versus transitory technologies: To ensure a successful data engineering approach, it is crucial to strike a balance between focusing on the rapidly evolving future and addressing current concrete needs. When selecting technologies, consider both immutable and transitory tools. Immutable technologies, like well-established languages and cloud components, have stood the test of time and are likely to remain relevant for a long time. Transitory technologies, on the other hand, may experience hype and popularity but could fade into obscurity quickly. Evaluating tools every two years and building around immutable technologies while considering transition barriers will help maintain flexibility and avoid potential pitfalls in the ever-changing data landscape.

- Location (cloud, on prem, hybrid cloud, multicloud): 
Companies have various options for running their technology stacks, including on premises, in the cloud, hybrid cloud, and multicloud environments.
On-premises systems are still common for established companies, where they own and manage their hardware in data centers or leased colocation space.
The cloud offers a rental model, allowing companies to rent hardware and managed services from cloud providers like AWS, Azure, or Google Cloud, offering dynamic scaling and fast project launches.
The cloud evolved from infrastructure as a service (IaaS) to platform as a service (PaaS) and software as a service (SaaS) offerings, providing managed services and simplified deployments.
Cloud economics are complex, and understanding cloud pricing models is crucial for efficient cloud usage.

- Build versus buy:
  The debate between building and buying technology solutions revolves around control, expertise, Total Cost of Ownership (TCO), and whether the solution offers a competitive advantage.
The book suggests investing in building and customizing when it provides a competitive advantage; otherwise, utilize existing solutions in the market.
Two types of data engineers are distinguished: Type A focuses on building and customizing when necessary, while Type B leans towards using existing solutions and abstraction.
The trend in software adoption is shifting from top-down decisions by IT to bottom-up adoption by technical roles within a company.
Open Source Software (OSS) is freely available and can be modified, but it requires maintenance and support. Community-managed OSS relies on strong communities, while commercial OSS offers managed services.
Factors to consider when choosing OSS include mindshare, maturity, troubleshooting support, project management, team, roadmap, self-hosting and maintenance, and contributing back to the community.
Proprietary Walled Gardens include independent offerings and cloud platform proprietary service offerings.
Independent offerings are proprietary solutions offered by data tool companies and can work well as fully managed services.
Factors to consider with independent offerings include interoperability, mindshare, documentation and support, pricing, and the longevity of the company.
Cloud platform proprietary service offerings are proprietary services developed by cloud vendors, bundled to create an integrated ecosystem.
Consider performance versus price, purchase considerations, and the Total Cost of Ownership when evaluating cloud platform proprietary service offerings.
The advice is to focus on areas where building custom solutions will add significant value, and lean towards OSS and COSS as default options. Upskilling existing teams to use managed platforms can be beneficial. Understand the decision-making process for budget approval and choose wisely to avoid delays in technology implementation.

