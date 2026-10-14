"""Shared full report text (combined detailed research + student draft)."""

EXECUTIVE_SUMMARY = """\
Tata Motors Limited is the Tata Group's flagship automotive company and one of India's largest vehicle manufacturers. \
This report presents a complete study of its history, business segments, products, manufacturing systems, research areas, \
challenges, and internship relevance for a Diploma in Electronics and Communication Engineering.

According to public disclosures for FY2024–25, Tata Motors strengthened its position in commercial vehicles, recorded strong SUV growth in passenger vehicles, and maintained leadership in passenger electric vehicles. Milestones include over 6 million cumulative passenger vehicle sales, more than 200,000 cumulative EV sales, expansion at Sanand, and progress on a new manufacturing facility in Tamil Nadu. The company's multi-powertrain approach (petrol, diesel, CNG, electric, and alternate fuels) supports India's goals for safer, cleaner mobility."""

INTRO = """\
The automobile industry is one of the most important sectors of the Indian economy. It contributes to industrial development, \
employment generation, technological innovation, infrastructure development, and international trade. Within this industry, \
Tata Motors has established itself as a major automobile manufacturer with a strong presence in passenger vehicles, commercial \
vehicles, electric mobility, and vehicle engineering.

Tata Motors was established in 1945 as Tata Engineering and Locomotive Company Limited (TELCO). Initially, the company focused on \
manufacturing locomotives and engineering products. Over time, it expanded into commercial vehicles, passenger cars, sports utility \
vehicles (SUVs), buses, and electric vehicles. The company has contributed significantly to the development of the Indian automobile \
industry by introducing indigenous vehicle designs, expanding manufacturing capabilities, improving vehicle safety, and investing in \
sustainable mobility.

This research report examines Tata Motors' background, organisational development, products, manufacturing processes, achievements, \
business progress, and recent developments. It also studies the manufacturing methodologies used in automobile production and the \
importance of continuous improvement in maintaining quality, productivity, and customer satisfaction."""

ABOUT = """\
Tata Motors is a well-known automotive manufacturer associated with the Tata Group. Its operations cover the design, development, \
manufacturing, marketing, and servicing of a wide range of vehicles.

The company serves individual customers, businesses, logistics operators, public transport organisations, and industrial customers. \
Its vehicles are used for personal transportation, goods transportation, passenger transport, construction, mining, defence-related \
mobility, and specialised commercial applications.

Tata Motors has invested in research and development, vehicle electrification, connected technologies, safety engineering, and \
advanced manufacturing systems. It is widely recognised for building vehicles that balance affordability with improving safety and technology."""

OVERVIEW = """\
Tata Motors operates in a highly competitive industry where product quality, pricing, design, safety, technology, fuel efficiency, \
and after-sales service influence customer decisions. Its business is organised around major automotive segments reported publicly for \
the Tata Motors Group: Tata Commercial Vehicles (CV), Tata Passenger Vehicles (PV), electric mobility, and Jaguar Land Rover (JLR).

Effective 1 October 2025, a composite scheme of arrangement (approved by the National Company Law Tribunal) demerged commercial vehicles \
from passenger vehicles (including electric passenger mobility) to allow sharper focus and strategy execution in each business."""

SEGMENT_CV = [
    "Trucks (light, medium, heavy), tippers, and specialised haulage vehicles.",
    "Buses and staff carriers for public transport and institutions.",
    "Small commercial vehicles and pickups (Ace, Intra families).",
    "Electric commercial mobility including Ace EV and e-bus solutions.",
    "Market leadership in Indian CV with focus on uptime and total cost of ownership.",
]

SEGMENT_PV = [
    "Hatchbacks and sedans: Tiago, Altroz, Tigor.",
    "SUVs and crossovers: Punch, Nexon, Harrier, Safari, Curvv.",
    "Multi-powertrain strategy: petrol, diesel, CNG, and electric where offered.",
    "Safety and design are key brand pillars (including NCAP-focused marketing).",
]

SEGMENT_EV = [
    "Passenger EV leadership in India with Nexon EV, Tiago EV, Punch EV, and related platforms.",
    "ZIPTRON and acti.ev technology for range, safety, and charging ecosystem.",
    "Commercial electric buses and smart-city mobility solutions.",
]

SEGMENT_JLR = """\
Acquired in 2008, Jaguar Land Rover is Tata Motors' global premium automotive business with luxury brands, advanced engineering, \
and manufacturing primarily in the United Kingdom and other international locations."""

HISTORY = {
    "4.1 Early foundation: 1945": "Tata Motors was established in 1945 as Tata Engineering and Locomotive Company Limited. Its initial activities were associated with locomotives and engineering products, building industrial capability for later vehicle manufacturing.",
    "4.2 Entry into commercial vehicles: 1950s": "The company entered the commercial vehicle sector through collaboration with Daimler-Benz of Germany (1954), beginning organised truck manufacturing in India.",
    "4.3 Expansion into passenger vehicles": "Passenger vehicles helped the company move beyond commercial transport. The Tata Indica (1998) became a significant milestone as an indigenously developed passenger car and strengthened market presence.",
    "4.4 International expansion: 2000s": "In 2004, Tata Motors acquired Daewoo Commercial Vehicle Company in South Korea. In 2008, it acquired Jaguar Land Rover from Ford Motor Company—a landmark acquisition expanding luxury brands and global engineering.",
    "4.5 Development of modern vehicles": "In subsequent years, the company introduced products focused on styling, fuel efficiency, safety, comfort, and technology. Vehicles such as Tiago, Nexon, Harrier, Safari, and Punch strengthened the passenger portfolio. Tata Ace (2005) transformed last-mile logistics.",
    "4.6 Electric mobility and digital manufacturing": "Tata Motors invested in battery-electric vehicles, electric powertrains, charging partnerships, software-enabled features, and efficient manufacturing. FY2024–25 reporting highlights CNG and EV share growth, hydrogen ICE truck development, automation, and AI-enabled operations.",
}

MFG_INTRO = """\
Automobile manufacturing involves multiple coordinated activities, from product design and raw material procurement to assembly, \
inspection, and delivery. Tata Motors' exact procedures vary by plant, product, and production line. The following methodologies \
describe established automotive manufacturing practices relevant to its operations; they should not be interpreted as a verified list \
of systems used identically at every Tata Motors facility."""

MFG_SECTIONS = [
    ("5.1 Lean manufacturing", "Lean manufacturing aims to reduce waste and improve the flow of materials and work.", [
        "Eliminating unnecessary movement and waiting time.",
        "Reducing excess inventory.",
        "Improving workstation organisation.",
        "Simplifying manufacturing processes.",
        "Reducing defects and rework.",
        "Improving productivity without compromising quality.",
    ]),
    ("5.2 Just-in-Time (JIT) production", "Just-in-Time production supplies materials and components when required by the production process.", [
        "Requires reliable suppliers and accurate production schedules.",
        "Needs coordination between purchasing, stores, and assembly.",
    ]),
    ("5.3 Kaizen and continuous improvement", "Kaizen focuses on continuous, incremental improvement in safety, quality, productivity, and workflow.", []),
    ("5.4 Total Quality Management (TQM)", "TQM emphasises quality across the entire organisation—not only at final inspection.", [
        "Establishing quality standards.",
        "Training employees in correct procedures.",
        "Monitoring production defects.",
        "Investigating root causes of failures.",
    ]),
    ("5.5 Automation and robotics", "Automation improves precision, repeatability, and productivity in welding, painting, and assembly operations.", []),
    ("5.6 Computer-Aided Design and Manufacturing", "CAD supports digital vehicle design; CAM supports planning and execution of manufacturing operations.", []),
    ("5.7 Supply chain management", "Automobile manufacturing depends on suppliers of steel, tyres, electronics, batteries, glass, and seats.", [
        "Supplier evaluation and purchasing.",
        "Inventory planning and incoming inspection.",
        "Production scheduling and logistics coordination.",
    ]),
    ("5.8 Safety and environmental management", "Plants manage occupational safety, energy, emissions, waste, water, and chemical handling.", [
        "Machine guarding and safety training.",
        "Energy monitoring and waste segregation.",
        "Wastewater treatment and environmental compliance.",
    ]),
    ("5.9 Electric vehicle manufacturing", "EV production shares body, paint, and assembly processes with conventional vehicles but adds:", [
        "Battery pack assembly and thermal management.",
        "High-voltage components and electrical safety protocols.",
        "Electric motors and power electronics integration.",
    ]),
    ("5.10 Quality inspection and testing", "Before dispatch, manufacturers conduct multiple inspections and tests:", [
        "Body and paint inspection; dimensional checks.",
        "Electrical system and powertrain testing.",
        "Brake, steering, leak, and end-of-line functional tests.",
        "Road testing or prescribed vehicle checks.",
    ]),
]

PRODUCTS_INTRO = """\
Tata Motors has developed a wide range of vehicles for individual customers, businesses, and public transport operators. \
The portfolio is summarised in the table below and illustrated with representative product categories."""

PRODUCT_BLOCKS = [
    ("6.1 Passenger cars and SUVs", "product_passenger_suv.jpg",
     "Passenger vehicles are designed for personal and family transportation. Tata Motors offers hatchbacks, sedans, and SUVs with emphasis on safety, comfort, and fuel-efficient or electric powertrains. Representative models include Tiago, Altroz, Tigor, Punch, Nexon, Harrier, Safari, and Curvv."),
    ("6.2 Electric vehicles", "product_ev.jpg",
     "Electric vehicles use electric motors and rechargeable battery packs. Tata Motors is a leader in India's passenger EV segment with models such as Nexon EV, Tiago EV, Punch EV, and Tigor EV, supported by charging partnerships and evolving battery technology."),
    ("6.3 Commercial trucks", "product_truck.jpg",
     "Trucks support industrial, agricultural, and logistics transport. Tata Motors manufactures light, medium, and heavy commercial vehicles including Ace, Intra, Ultra, Signa, and Prima families for varied payload and distance requirements."),
    ("6.4 Buses and passenger transport vehicles", "product_bus.jpg",
     "Buses are used for city service, school transport, staff carriers, and intercity travel. Tata Motors supplies conventional and electric bus solutions for public transport operators and smart-city mobility programmes."),
]

PRODUCT_TABLE = [
    ("Passenger", "Hatch / sedan", "Tiago, Altroz, Tigor"),
    ("Passenger", "SUV / crossover", "Punch, Nexon, Harrier, Safari, Curvv"),
    ("Commercial", "SCV / LCV / M&HCV", "Ace, Intra, Ultra, Prima, Signa"),
    ("Commercial", "Buses", "Starbus, electric buses"),
    ("Electric", "Passenger & CV EV", "Nexon EV, Tiago EV, Punch EV, Ace EV"),
]

ECE = """\
Modern automobiles are complex electro-mechanical systems. Electronics and Communication Engineering plays an important role in automotive R&D and production quality at Tata Motors.

Key domains include engine control units (ECU), body control modules, infotainment and telematics, ADAS sensors, battery management systems (BMS) in EVs, wiring harnesses, in-vehicle networks (CAN, LIN, Ethernet in newer architectures), and over-the-air software updates.

During authorised plant visits or internships, diploma students may observe trim-and-chassis processes, harness routing, earthing safety checks, ECU flashing, heating-element quality, connector inspection, PLC-based automation, robotic welding cells, and end-of-line electrical testing—especially at passenger vehicle plants such as Pune and manufacturing locations such as Sanand and Jamshedpur."""

PLANTS = """\
Tata Motors operates major manufacturing and assembly facilities in India including Pune (passenger vehicles), Jamshedpur and Lucknow (commercial vehicles), Sanand (passenger and EV-related capacity), and Dharwad. Typical plant flow includes stamping, body shop, paint shop, engine or powertrain assembly (where applicable), final assembly, and quality gates before dispatch."""

CHALLENGES_INTRO = """\
Tata Motors operates in an industry affected by intense competition, changing customer preferences, raw material costs, supply chain risks, technology transitions, and environmental regulations. New technologies create opportunities but require investment in engineering, testing, production equipment, and workforce skills."""

CHALLENGES = [
    "Competition and pricing: Manufacturers must balance product features, affordability, quality, and profitability.",
    "Supply chain resilience: Component shortages or delayed deliveries can interrupt production.",
    "Quality and reliability: Defects can increase rework, warranty costs, and customer dissatisfaction.",
    "Electrification: Battery cost, charging infrastructure, range, resale value, and customer confidence influence EV adoption.",
    "Sustainability and compliance: Manufacturers must respond to changing safety, emission, and environmental requirements.",
    "Future opportunities: Further R&D, process digitalisation, improved energy efficiency, battery recycling, and data-driven quality improvement.",
]

METHODOLOGY = """\
This report uses a descriptive, document-based research approach. It organises publicly available company information and general automotive manufacturing knowledge to understand Tata Motors' development, products, R&D areas, manufacturing methodologies, and challenges."""

METHODOLOGY_BULLETS = [
    "Secondary data: Official company information, annual reports, investor materials, product catalogues, government publications, and reputable automotive industry sources.",
    "Primary data (if collected): Direct observation, authorised employee interviews, permitted document review, or discussions during an industrial visit.",
    "Data analysis: Historical analysis for company development; descriptive analysis for products and processes; thematic analysis for quality, manufacturing, sustainability, and challenges.",
    "Verification: Compare information across sources; record publication dates and financial year for quantitative claims.",
    "Limitations: Public sources may not disclose confidential plant procedures, detailed production data, or team-level R&D work.",
]

CONCLUSION = """\
Tata Motors has grown from a locomotive and engineering company into a diversified automotive group with leadership in Indian commercial vehicles, a strong passenger vehicle portfolio, market-leading electric mobility initiatives, and a global premium business through Jaguar Land Rover.

Its manufacturing philosophy combines lean production, quality systems, automation, supply chain coordination, and increasing digitalisation. For diploma students—especially in Electronics and Communication Engineering—studying Tata Motors provides practical insight into large-scale manufacturing, vehicle electronics integration, safety culture, and sustainable mobility aligned with national industrial growth."""

REFERENCES = [
    "Tata Motors Limited, Integrated Annual Report 2024–25.",
    "Tata Motors Limited, Q4 FY25 Investor Presentation and press releases.",
    "Tata Motors Limited, Corporate website — www.tatamotors.com",
    "Tata Motors Careers, Student Programmes — joinus.tatamotors.com",
    "Government of India automotive sector publications (industry context).",
]
