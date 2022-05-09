from .action_impls import (
    AdvancedScreeningTechnologyAction,
    AICentralAction,
    AssetLiquidationAction,
    BrainstormingSessionAction,
    CircuitBoardFactoryAction,
    ConservedBiomeAction,
    DecomposingFungusAction,
    DevelopedInfrastructureAction,
    DevelopmentCenterAction,
    ExtremeColdFungusAction,
    FarmersMarketAction,
    GHGProducingBacteriaAction,
    GreenhousesAction,
    HydroElectricEnergyAction,
    MatterManufacturingAction,
    NitriteReducingBacteriaAction,
    PowerInfrastructureAction,
    RegolithEatersAction,
    SolarpunkAction,
    ThinkTankAction,
    VolcanicPoolsAction,
    WaterImportFromEuropaAction,
    WoodBurningStovesAction,
    MatterGeneratorAction,
    ProgressivePoliciesAction,
    SelfReplicatingBacteriaAction,
)
from .card import ProjectCard, BlueProjectCard, GreenProjectCard, RedProjectCard
from .card_requirements import (
    CardRequirementsUnion,
    RedBlueTagRequirements,
    GreenTagRequirements,
    RedBlueGlobalParameterRequirements,
    GreenGlobalParameterRequirements,
    RedBlueSpendRequirements,
    GreenSpendRequirements,
)
from .global_requirements import GlobalParameterColor, Oceans, Oxygen, Temperature
from .enums import SpendRequirementType, Tag

AdaptationTechnology = BlueProjectCard(
    name="Adaptation Technology",
    cost=12,
    tags=[Tag.Science],
    points=1,
)
AdvancedAlloys = BlueProjectCard(
    name="Advanced Alloys",
    cost=9,
    tags=[Tag.Building],
)
AdvancedScreeningTechnology = BlueProjectCard(
    name="Advanced Screening Technology",
    cost=6,
    tags=[Tag.Science],
    action=AdvancedScreeningTechnologyAction(),
)
AICentral = BlueProjectCard(
    name="AI Central",
    cost=22,
    tags=[Tag.Science, Tag.Building],
    points=2,
    action=AICentralAction(),
    requirements=RedBlueTagRequirements(minimum=5, tag=Tag.Science),
)
AnaerobicMicroorganisms = BlueProjectCard(
    name="Anaerobic Microorganisms",
    cost=10,
    tags=[Tag.Microbe],
)
AntiGravityTechnology = BlueProjectCard(
    name="Anti-Gravity Technology",
    cost=18,
    tags=[Tag.Science],
    points=3,
    requirements=RedBlueTagRequirements(minimum=5, tag=Tag.Science),
)
AquiferPumping = BlueProjectCard(
    name="Aquifer Pumping", cost=14, tags=[Tag.Building], action=AquiferPumpingAction()
)
ArcticAlgae = BlueProjectCard(
    name="Arctic Algae",
    cost=19,
    tags=[Tag.Plant],
    points=2,
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
ArtificialJungle = BlueProjectCard(
    name="Artificial Jungle", cost=5, action=ArtificialJungleAction()
)
AssemblyLines = BlueProjectCard(
    name="Assembly Lines",
    cost=13,
    tags=[Tag.Space],
)
AssetLiquidation = BlueProjectCard(
    name="Asset Liquidation",
    cost=0,
    tags=[Tag.Science],
    action=AssetLiquidationAction(),
)
Birds = BlueProjectCard(
    name="Birds",
    cost=15,
    tags=[Tag.Animal],
    points=None,
    action=BirdsAction(),
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.White,
        maximum=GlobalParameterColor.White,
    ),
)
BrainstormingSession = BlueProjectCard(
    name="Brainstorming Session",
    cost=8,
    tags=[Tag.Space],
    action=BrainstormingSessionAction(),
)
CaretakerContract = BlueProjectCard(
    name="Caretaker Contract",
    cost=18,
    tags=[],
    action=CaretakerContractAction(),
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Yellow,
        maxmium=GlobalParameterColor.White,
    ),
)
CircuitBoardFactory = BlueProjectCard(
    name="Circuit Board Factory",
    cost=14,
    tags=[Tag.Building],
    action=CircuitBoardFactoryAction(),
)
CommunityGardens = BlueProjectCard(
    name="Community Gardens", cost=20, tags=[Tag.Plant], action=CommunityGardensAction()
)
CompostingFactory = BlueProjectCard(
    name="Composting Factory",
    cost=13,
    tags=[Tag.Building],
    points=1,
)
ConservedBiome = BlueProjectCard(
    name="Conserved Biome",
    cost=25,
    tags=[Tag.Building, Tag.Microbe, Tag.Animal],
    points=None,
    action=ConservedBiomeAction(),
)
Decomposers = BlueProjectCard(
    name="Decomposers",
    cost=7,
    tags=[Tag.Microbe],
    points=1,
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
DecomposingFungus = BlueProjectCard(
    name="Decomposing Fungus",
    cost=10,
    tags=[Tag.Microbe],
    action=DecomposingFungusAction(),
)
DevelopedInfrastructure = BlueProjectCard(
    name="Developed Infrastructure",
    cost=12,
    tags=[],
    points=1,
    action=DevelopedInfrastructureAction(),
)
DevelopmentCenter = BlueProjectCard(
    name="Development Center",
    cost=7,
    tags=[Tag.Science, Tag.Building],
    action=DevelopmentCenterAction(),
)
EarthCatapult = BlueProjectCard(
    name="Earth Catapult",
    cost=24,
    tags=[Tag.Building, Tag.Earth],
    points=2,
)
EcologicalZone = BlueProjectCard(
    name="Ecological Zone",
    cost=11,
    tags=[Tag.Plant, Tag.Animal],
    points=None,
)
EnergySubsidies = BlueProjectCard(
    name="Energy Subsidies",
    cost=5,
    tags=[Tag.Space],
)
ExtendedResources = BlueProjectCard(
    name="Extended Resources",
    cost=10,
    tags=[Tag.Science, Tag.Building],
)
ExtremeColdFungus = BlueProjectCard(
    name="Extreme-Cold Fungus",
    cost=10,
    tags=[Tag.Microbe],
    action=ExtremeColdFungusAction(),
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Purple,
        maxmium=GlobalParameterColor.Purple,
    ),
)
FarmersMarket = BlueProjectCard(
    name="Farmers Market",
    cost=12,
    tags=[Tag.Plant],
    points=1,
    action=FarmersMarketAction(),
)
FarmingCoOps = BlueProjectCard(
    name="Farming Co-ops", cost=15, tags=[Tag.Plant], action=FarmingCoOpsAction()
)
Fish = BlueProjectCard(
    name="Fish",
    cost=11,
    tags=[Tag.Animal],
    points=None,
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
GHGProducingBacteria = BlueProjectCard(
    name="GHG Producing Bacteria",
    cost=10,
    tags=[Tag.Science.Microbe],
    action=GHGProducingBacteriaAction(),
)
Greenhouses = BlueProjectCard(
    name="Greenhouses",
    cost=11,
    tags=[Tag.Building, Tag.Plant],
    action=GreenhousesAction(),
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Yellow,
        maxmium=GlobalParameterColor.White,
    ),
)
Herbivores = BlueProjectCard(
    name="Herbivores",
    cost=25,
    tags=[Tag.Animal],
    points=None,
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Oceans, minimum=5, maximum=9
    ),
)
HydroElectricEnergy = BlueProjectCard(
    name="Hydro-Electric Energy",
    cost=11,
    tags=[Tag.Building],
    action=HydroElectricEnergyAction(),
)
InterplenetaryRelations = BlueProjectCard(
    name="Interplenetary Relations",
    cost=35,
    tags=[Tag.Space, Tag.Jovian],
    points=None,
)
Interns = BlueProjectCard(
    name="Interns",
    cost=3,
    tags=[Tag.Science],
)
InterplanetaryConference = BlueProjectCard(
    name="Interplanetary Conference",
    cost=6,
    tags=[Tag.Earth],
)
Ironworks = BlueProjectCard(
    name="Ironworks", cost=12, tags=[Tag.Building], action=IronworksAction()
)
Livestock = BlueProjectCard(
    name="Livestock",
    cost=15,
    tags=[Tag.Animal],
    points=None,
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Yellow,
        maxmium=GlobalParameterColor.White,
    ),
)
MarsUniversity = BlueProjectCard(
    name="Mars University",
    cost=10,
    tags=[Tag.Science, Tag.Buildimg],
    points=1,
)
MatterManufacturing = BlueProjectCard(
    name="Matter Manufacturing",
    cost=9,
    tags=[Tag.Science],
    action=MatterManufacturingAction(),
)
MediaGroup = BlueProjectCard(
    name="Media Group",
    cost=11,
    tags=[Tag.Earth],
)
NitriteReducingBacteria = BlueProjectCard(
    name="Nitrite Reducing Bacteria",
    cost=11,
    tags=[Tag.Microbe],
    action=NitriteReducingBacteriaAction(),
)
OlympusConference = BlueProjectCard(
    name="Olympus Conference",
    cost=15,
    tags=[Tag.Science, Tag.Building, Tag.Earth],
    points=1,
)
OptimalAerobraking = BlueProjectCard(
    name="Optimal Aerobraking",
    cost=10,
    tags=[Tag.Space],
)
PhysicsComplex = BlueProjectCard(
    name="Physics Complex",
    cost=5,
    tags=[Tag.Science, Tag.Building],
    points=None,
    requirements=RedBlueTagRequirements(minimum=4, tag=Tag.Science),
)
PowerInfrastructure = BlueProjectCard(
    name="Power Infrastructure",
    cost=4,
    tags=[Tag.Building, Tag.Power],
    action=PowerInfrastructureAction(),
)
RecycledDetritus = BlueProjectCard(
    name="Recycled Detritus",
    cost=24,
    tags=[],
    points=1,
)
RedraftedContracts = BlueProjectCard(
    name="Redrafted Contracts", cost=4, tags=[], action=RedraftedContractsAction()
)
RegolithEaters = BlueProjectCard(
    name="Regolith Eaters",
    cost=10,
    tags=[Tag.Science, Tag.Microbe],
    action=RegolithEatersAction(),
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
ResearchOutpost = BlueProjectCard(
    name="Research Outpost",
    cost=6,
    tags=[Tag.Science, Tag.Building],
)
RestructuredResources = BlueProjectCard(
    name="Restructured Resources",
    cost=7,
    tags=[],
)
SmallAnimals = BlueProjectCard(
    name="Small Animals",
    cost=9,
    tags=[Tag.Animal],
    points=None,
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
Solarpunk = BlueProjectCard(
    name="Solarpunk",
    cost=15,
    tags=[Tag.Space, Tag.Plant],
    points=1,
    action=SolarpunkAction(),
)
StandardTechnology = BlueProjectCard(
    name="Standard Technology",
    cost=15,
    tags=[Tag.Science],
    points=1,
)
Steelworks = BlueProjectCard(
    name="Steelworks", cost=15, tags=[Tag.Building], points=1, action=SteelworksAction()
)
SymbioticFungus = BlueProjectCard(
    name="Symbiotic Fungus",
    cost=3,
    tags=[Tag.Microbe],
    action=SymbioticFungusAction(),
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
Tardigrades = BlueProjectCard(
    name="Tardigrades",
    cost=6,
    tags=[Tag.Microbe],
    points=None,
)
ThinkTank = BlueProjectCard(
    name="Think Tank",
    cost=13,
    tags=[Tag.Science],
    points=None,
    action=ThinkTankAction(),
)
UnitedPlanetaryAlliance = BlueProjectCard(
    name="United Planetary Alliance",
    cost=11,
    tags=[Tag.Science, Tag.Earth],
)
ViralEnhancers = BlueProjectCard(
    name="Viral Enhancers",
    cost=8,
    tags=[Tag.Microbe, Tag.Plant],
)
VolcanicPools = BlueProjectCard(
    name="Volcanic Pools",
    cost=17,
    tags=[Tag.Space],
    points=1,
    action=VolcanicPoolsAction(),
)
WaterImportFromEuropa = BlueProjectCard(
    name="Water Import from Europa",
    cost=22,
    tags=[Tag.Space, Tag.Jovian],
    points=None,
    action=WaterImportFromEuropaAction(),
)
WoodBurningStoves = BlueProjectCard(
    name="Wood Burning Stoves",
    cost=13,
    tags=[Tag.Building],
    action=WoodBurningStovesAction(),
)
AdvancedEcosystems = RedProjectCard(
    name="Advanced Ecosystems",
    cost=10,
    tags=[Tag.Microbe, Tag.Animal, Tag.Event],
    points=3,
    requirements=CardRequirementsUnion(
        RedBlueTagRequirements(minimum=1, tag=Tag.Animal),
        RedBlueTagRequirements(minimum=1, tag=Tag.Microbe),
        RedBlueTagRequirements(minimum=1, tag=Tag.Plant),
    ),
)
ArtificialLake = RedProjectCard(
    name="Artificial Lake",
    cost=13,
    tags=[Tag.Event],
    points=1,
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Yellow,
        maxmium=GlobalParameterColor.White,
    ),
)
AtmosphereFiltering = RedProjectCard(
    name="Atmosphere Filtering",
    cost=6,
    tags=[Tag.Space, Tag.Event],
    requirements=RedBlueTagRequirements(minimum=2, tag=Tag.Science),
)
BreathingFilters = RedProjectCard(
    name="Breathing Filters",
    cost=9,
    tags=[Tag.Event],
    points=2,
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Yellow,
        maxmium=GlobalParameterColor.White,
    ),
)
BribedCommittee = RedProjectCard(
    name="Bribed Committee",
    cost=5,
    tags=[Tag.Earth, Tag.Event],
    points=-2,
)
BusinessContacts = RedProjectCard(
    name="Business Contacts",
    cost=5,
    tags=[Tag.Earth, Tag.Event],
)
CeoSFavoriteProject = RedProjectCard(
    name="CEOs Favorite Project",
    cost=3,
    tags=[Tag.Event],
)
ColonizerTrainingCamp = RedProjectCard(
    name="Colonizer Training Camp",
    cost=10,
    tags=[Tag.Building, Tag.Jovian, Tag.Event],
    points=2,
    requirements=RedBlueRedBlueGlobalParameterRequirements(
        parameter_type=Oxygen,
        maximum=GlobalParameterColor.Red,
        minium=GlobalParameterColor.Purple,
    ),
)
Comet = RedProjectCard(
    name="Comet",
    cost=25,
    tags=[Tag.Space, Tag.Event],
)
ConvoyFromEuropa = RedProjectCard(
    name="Convoy from Europa",
    cost=14,
    tags=[Tag.Space, Tag.Event],
)
Crater = RedProjectCard(
    name="Crater",
    cost=7,
    tags=[Tag.Event],
    requirements=RedBlueTagRequirements(minimum=3, tag=Tag.Event),
)
DeimosDown = RedProjectCard(
    name="Deimos Down",
    cost=30,
    tags=[Tag.Space, Tag.Event],
)
GiantIceAsteroid = RedProjectCard(
    name="Giant Ice Asteroid",
    cost=36,
    tags=[Tag.Space, Tag.Event],
)
IceAsteroid = RedProjectCard(
    name="Ice Asteroid",
    cost=21,
    tags=[Tag.Space, Tag.Event],
)
IceCapMelting = RedProjectCard(
    name="Ice Cap Melting",
    cost=4,
    tags=[Tag.Event],
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.White,
        maximum=GlobalParameterColor.White,
    ),
)
ImportedHydrogen = RedProjectCard(
    name="Imported Hydrogen",
    cost=17,
    tags=[Tag.Space, Tag.Earth, Tag.Event],
)
ImportedNitrogen = RedProjectCard(
    name="Imported Nitrogen",
    cost=20,
    tags=[Tag.Space, Tag.Earth, Tag.Event],
)
InterstellarColonuShip = RedProjectCard(
    name="Interstellar Colonu Ship",
    cost=20,
    tags=[Tag.Space, Tag.Earth, Tag.Event],
    points=4,
    requirements=RedBlueTagRequirements(minimum=4, tag=Tag.Science),
)
InventionContest = RedProjectCard(
    name="Invention Contest",
    cost=1,
    tags=[Tag.Science, Tag.Event],
)
InvestmentLoan = RedProjectCard(
    name="Investment Loan",
    cost=1,
    tags=[Tag.Earth, Tag.Evvent],
    points=1,
    requirements=RedBlueSpendRequirements(
        cost=1, req_type=SpendRequirementType.TerraformingRating
    ),
)
LagrangeObservatory = RedProjectCard(
    name="Lagrange Observatory",
    cost=7,
    tags=[Tag.Science, Tag.Space, Tag.Event],
    points=1,
)
LakeMarineris = RedProjectCard(
    name="Lake Marineris",
    cost=17,
    tags=[Tag.Event],
    points=1,
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Yellow,
        maxmium=GlobalParameterColor.White,
    ),
)
LargeConvoy = RedProjectCard(
    name="Large Convoy",
    cost=36,
    tags=[Tag.Space, Tag.Earth, Tag.Event],
    points=2,
)
LavaFlows = RedProjectCard(
    name="Lava Flows",
    cost=17,
    tags=[Tag.Event],
)
LocalHeatTrapping = RedProjectCard(
    name="Local Heat Trapping",
    cost=0,
    tags=[Tag.Event],
    requirements=RedBlueSpendRequirements(cost=3, req_type=SpendRequirementType.Heat),
)
Mangrove = RedProjectCard(
    name="Mangrove",
    cost=12,
    tags=[Tag.Plant, Tag.Event],
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.White,
        maximum=GlobalParameterColor.White,
    ),
)
NitrogenRichAsteroid = RedProjectCard(
    name="Nitrogen-Rich Asteroid",
    cost=30,
    tags=[Tag.Space, Tag.Event],
)
PermafrostExtraction = RedProjectCard(
    name="Permafrost Extraction",
    cost=8,
    tags=[Tag.Event],
    requirements=RedBlueGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Yellow,
        maxmium=GlobalParameterColor.White,
    ),
)
PhobosFalls = RedProjectCard(
    name="Phobos Falls",
    cost=32,
    tags=[Tag.Space, Tag.Event],
    points=1,
)
Plantation = RedProjectCard(
    name="Plantation",
    cost=22,
    tags=[Tag.Plant, Tag.Event],
    requirements=RedBlueTagRequirements(minimum=4, tag=Tag.Science),
)
ReleaseOfInertGases = RedProjectCard(
    name="Release of Inert Gases",
    cost=16,
    tags=[Tag.Event],
)
Research = RedProjectCard(
    name="Research",
    cost=5,
    tags=[Tag.Science, Tag.Science, Tag.Event],
)
SpecialDesign = RedProjectCard(
    name="Special Design",
    cost=3,
    tags=[Tag.Event],
)
SubterraneanReservoir = RedProjectCard(
    name="Subterranean Reservoir",
    cost=10,
    tags=[Tag.Event],
)
TechnologyDemonstration = RedProjectCard(
    name="Technology Demonstration",
    cost=17,
    tags=[Tag.Science, Tag.Space, Tag.Event],
)
TerraformingGanymede = RedProjectCard(
    name="Terraforming Ganymede",
    cost=28,
    tags=[Tag.Space, Tag.Jovian, Tag.Event],
    points=2,
)
TowingAComet = RedProjectCard(
    name="Towing a Comet",
    cost=22,
    tags=[Tag.Space, Tag.Event],
)
WorkCrews = RedProjectCard(
    name="Work Crews",
    cost=5,
    tags=[Tag.Event],
)
AcquiredCompany = GreenProjectCard(
    name="Acquired Company",
    cost=11,
    tags=[Tag.Building, Tag.Earth],
)
AdaptedLichen = GreenProjectCard(
    name="Adapted Lichen",
    cost=6,
    tags=[Tag.Microbe, Tag.Plant],
)
AeratedMagma = GreenProjectCard(
    name="Aerated Magma",
    cost=18,
    tags=[Tag.Power],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
AirborneRadiation = GreenProjectCard(
    name="Airborne Radiation",
    cost=15,
    tags=[Tag.Earth],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
Algae = GreenProjectCard(
    name="Algae",
    cost=9,
    tags=[Tag.Plant],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oceans, minimum=5, maximum=9
    ),
)
Archaebacteria = GreenProjectCard(
    name="Archaebacteria",
    cost=5,
    tags=[Tag.Microbe],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Purple,
        maxmium=GlobalParameterColor.Purple,
    ),
)
ArtificialPhotosynthesis = GreenProjectCard(
    name="Artificial Photosynthesis",
    cost=11,
    tags=[Tag.Science],
)
AsteroidMining = GreenProjectCard(
    name="Asteroid Mining",
    cost=28,
    tags=[Tag.Space, Tag.Jovian],
    points=2,
)
AsteroidMiningConsortium = GreenProjectCard(
    name="Asteroid Mining Consortium",
    cost=6,
    tags=[],
)
Astrofarm = GreenProjectCard(
    name="Astrofarm",
    cost=21,
    tags=[Tag.Space],
)
AtosphericInsulators = GreenProjectCard(
    name="Atospheric Insulators",
    cost=10,
    tags=[Tag.Space, Tag.Earth],
)
AutomatedFactories = GreenProjectCard(
    name="Automated Factories",
    cost=18,
    tags=[Tag.Building],
)
BalancedPortfolios = GreenProjectCard(
    name="Balanced Portfolios",
    cost=8,
    tags=[Tag.Science],
    points=1,
    requirements=GreenSpendRequirements(
        cost=1, req_type=SpendRequirementType.TerraformingRating
    ),
)
BeamFromAThoriumAsteroid = GreenProjectCard(
    name="Beam from a Thorium Asteroid",
    cost=23,
    tags=[Tag.Space, Tag.Jovian, Tag.Power],
    points=1,
    requirements=GreenGreenTagRequirements(minimum=1, tag=Tag.Jovian),
)
BiomassCombustors = GreenProjectCard(
    name="Biomass Combustors",
    cost=15,
    tags=[Tag.Building, Tag.Power],
    requirements=GreenSpendRequirements(cost=2, req_type=SpendRequirementType.Plants),
)
BiothermalPower = GreenProjectCard(
    name="Biothermal Power",
    cost=18,
    tags=[Tag.Space, Tag.Power],
)
Blueprints = GreenProjectCard(
    name="Blueprints",
    cost=17,
    tags=[Tag.Earth],
)
BuildingIndustries = GreenProjectCard(
    name="Building Industries",
    cost=6,
    tags=[Tag.Building],
    requirements=GreenSpendRequirements(cost=4, req_type=SpendRequirementType.Heat),
)
Bushes = GreenProjectCard(
    name="Bushes",
    cost=13,
    tags=[Tag.Plant],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
CallistoPenalMines = GreenProjectCard(
    name="Callisto Penal Mines",
    cost=20,
    tags=[Tag.Building, Tag.Space, Tag.Jovian],
    points=1,
)
Cartel = GreenProjectCard(
    name="Cartel",
    cost=6,
    tags=[Tag.Earth],
)
CoalImports = GreenProjectCard(
    name="Coal Imports",
    cost=13,
    tags=[Tag.Building],
)
CommercialDistrict = GreenProjectCard(
    name="Commercial District",
    cost=25,
    tags=[Tag.Building],
)
DeepWellHeating = GreenProjectCard(
    name="Deep Well Heating",
    cost=14,
    tags=[Tag.Building, Tag.Power],
)
DesignedMicroorganisms = GreenProjectCard(
    name="Designed Microorganisms",
    cost=15,
    tags=[Tag.Science, Tag.Microbe],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        maximum=GlobalParameterColor.Red,
        minium=GlobalParameterColor.Purple,
    ),
)
DiversifiedInterests = GreenProjectCard(
    name="Diversified Interests",
    cost=15,
    tags=[Tag.Plant],
)
DustyQuarry = GreenProjectCard(
    name="Dusty Quarry",
    cost=2,
    tags=[],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oceans, minimum=0, maximum=3
    ),
)
EconomicGrowth = GreenProjectCard(
    name="Economic Growth",
    cost=10,
    tags=[Tag.Building],
)
EnergyStorage = GreenProjectCard(
    name="Energy Storage",
    cost=18,
    tags=[Tag.Power],
    requirements=GreenSpendRequirements(
        cost=7, req_type=SpendRequirementType.TerraformingRating, spend=False
    ),
)
EosChasmaNationalPark = GreenProjectCard(
    name="Eos Chasma National Park",
    cost=16,
    tags=[Tag.Building, Tag.Plant],
    points=1,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
Farming = GreenProjectCard(
    name="Farming",
    cost=20,
    tags=[Tag.Plant],
    points=2,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.White,
        maximum=GlobalParameterColor.White,
    ),
)
FoodFactory = GreenProjectCard(
    name="Food Factory",
    cost=9,
    tags=[Tag.Building],
    requirements=GreenSpendRequirements(cost=2, req_type=SpendRequirementType.Plants),
)
FuelFactory = GreenProjectCard(
    name="Fuel Factory",
    cost=9,
    tags=[Tag.Building],
    requirements=GreenSpendRequirements(cost=3, req_type=SpendRequirementType.Heat),
)
FueledGenerators = GreenProjectCard(
    name="Fueled Generators",
    cost=4,
    tags=[Tag.Building, Tag.Power],
    requirements=GreenSpendRequirements(
        cost=1, req_type=SpendRequirementType.TerraformingRating
    ),
)
FusionPower = GreenProjectCard(
    name="Fusion Power",
    cost=7,
    tags=[Tag.Science, Tag.Building, Tag.Power],
    requirements=GreenGreenTagRequirements(minimum=2, tag=Tag.Power),
)
GanymedeShipyard = GreenProjectCard(
    name="Ganymede Shipyard",
    cost=17,
    tags=[Tag.Space, Tag.Jovian],
)
GeneRepair = GreenProjectCard(
    name="Gene Repair",
    cost=15,
    tags=[Tag.Science],
    points=2,
    requirements=GreenTagRequirements(minimum=3, tag=Tag.Science),
)
GeothermalPower = GreenProjectCard(
    name="Geothermal Power",
    cost=8,
    tags=[Tag.Building, Tag.Power],
)
GiantSpaceMirror = GreenProjectCard(
    name="Giant Space Mirror",
    cost=13,
    tags=[Tag.Space, Tag.Power],
)
Grass = GreenProjectCard(
    name="Grass",
    cost=9,
    tags=[Tag.Plant],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
GreatDam = GreenProjectCard(
    name="Great Dam",
    cost=12,
    tags=[Tag.Building, Tag.Power],
    points=1,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oceans, minimum=2, maximum=9
    ),
)
GreatEscarpmentConsortium = GreenProjectCard(
    name="Great Escarpment Consortium",
    cost=3,
    tags=[],
)
Heather = GreenProjectCard(
    name="Heather",
    cost=14,
    tags=[Tag.Plant],
    points=1,
)
ImmigrationShuttles = GreenProjectCard(
    name="Immigration Shuttles",
    cost=20,
    tags=[Tag.Space, Tag.Earth],
    points=None,
)
ImportOfAdvancedGHG = GreenProjectCard(
    name="Import of Advanced GHG",
    cost=8,
    tags=[Tag.Space, Tag.Earth],
)
ImportedGHG = GreenProjectCard(
    name="Imported GHG",
    cost=8,
    tags=[Tag.Earth],
)
IndustrialCenter = GreenProjectCard(
    name="Industrial Center",
    cost=15,
    tags=[Tag.Building],
)
IndustiralFarming = GreenProjectCard(
    name="Industiral Farming",
    cost=19,
    tags=[Tag.Building],
)
IndustrialMicrobes = GreenProjectCard(
    name="Industrial Microbes",
    cost=9,
    tags=[Tag.Building, Tag.Microbe],
)
Insects = GreenProjectCard(
    name="Insects",
    cost=10,
    tags=[Tag.Microbe],
)
IoMiningIndustries = GreenProjectCard(
    name="Io Mining Industries",
    cost=37,
    tags=[Tag.Building, Tag.Space, Tag.Jovian],
)
KelpFarming = GreenProjectCard(
    name="Kelp Farming",
    cost=17,
    tags=[],
    points=1,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oceans, minimum=6, maximum=9
    ),
)
Lichen = GreenProjectCard(
    name="Lichen",
    cost=5,
    tags=[Tag.Plant],
)
LightningHarvest = GreenProjectCard(
    name="Lightning Harvest",
    cost=13,
    tags=[Tag.Science, Tag.Power],
    points=1,
)
LowAtmoShields = GreenProjectCard(
    name="Low-Atmo Shields",
    cost=9,
    tags=[Tag.Building],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
LunarBeam = GreenProjectCard(
    name="Lunar Beam",
    cost=9,
    tags=[Tag.Earth, Tag.Power],
    requirements=GreenSpendRequirements(
        cost=1, req_type=SpendRequirementType.TerraformingRating
    ),
)
MassConverter = GreenProjectCard(
    name="Mass Converter",
    cost=20,
    tags=[Tag.Science, Tag.Building, Tag.Power],
    points=2,
    requirements=GreenTagRequirements(minimum=4, tag=Tag.Science),
)
MedicalLab = GreenProjectCard(
    name="Medical Lab",
    cost=15,
    tags=[Tag.Building],
    points=1,
)
MethaneFromTitan = GreenProjectCard(
    name="Methane from Titan",
    cost=35,
    tags=[Tag.Space, Tag.Jovian],
    points=2,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
MicroMills = GreenProjectCard(
    name="Micro-Mills",
    cost=9,
    tags=[Tag.Building],
)
Microprocessors = GreenProjectCard(
    name="Microprocessors",
    cost=17,
    tags=[Tag.Building, Tag.Power],
)
Mine = GreenProjectCard(
    name="Mine",
    cost=10,
    tags=[Tag.Building],
)
MirandaResort = GreenProjectCard(
    name="Miranda Resort",
    cost=15,
    tags=[Tag.Space, Tag.Earth, Tag.Jovian],
    points=1,
)
MoholeArea = GreenProjectCard(
    name="Mohole Area",
    cost=18,
    tags=[Tag.Building],
)
Monocultures = GreenProjectCard(
    name="Monocultures",
    cost=6,
    tags=[],
    requirements=GreenSpendRequirements(
        cost=1, req_type=SpendRequirementType.TerraformingRating
    ),
)
Moss = GreenProjectCard(
    name="Moss",
    cost=3,
    tags=[Tag.Plant],
    requirements=CardRequirementsUnion(
        GreenGlobalParameterRequirements(parameter_type=Oceans, minimum=3, maximum=9),
        GreenSpendRequirements(cost=1, req_type=SpendRequirementType.Plants),
    ),
)
NaturalPreserve = GreenProjectCard(
    name="Natural Preserve",
    cost=12,
    tags=[Tag.Science, Tag.Building],
    points=1,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
NewPortfolios = GreenProjectCard(
    name="New Portfolios",
    cost=14,
    tags=[Tag.Plant, Tag.Power],
)
NitrophilicMoss = GreenProjectCard(
    name="Nitrophilic Moss",
    cost=14,
    tags=[Tag.Plant],
)
NoctisFarming = GreenProjectCard(
    name="Noctis Farming",
    cost=13,
    tags=[Tag.Building, Tag.Plant],
    points=1,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
NuclearPlants = GreenProjectCard(
    name="Nuclear Plants",
    cost=10,
    tags=[Tag.Building],
    points=-1,
)
PowerGrid = GreenProjectCard(
    name="Power Grid",
    cost=8,
    tags=[Tag.Building, Tag.Power],
)
PowerPlant = GreenProjectCard(
    name="Power Plant",
    cost=3,
    tags=[Tag.Building, Tag.Power],
)
PowerSupplyConsortium = GreenProjectCard(
    name="Power Supply Consortium",
    cost=12,
    tags=[Tag.Power],
)
ProtectedValley = GreenProjectCard(
    name="Protected Valley",
    cost=22,
    tags=[Tag.Building, Tag.Plant],
)
QuantumExtractor = GreenProjectCard(
    name="Quantum Extractor",
    cost=16,
    tags=[Tag.Science, Tag.Building, Tag.Power],
    requirements=GreenTagRequirements(minimum=3, tag=Tag.Science),
)
RadSuits = GreenProjectCard(
    name="Rad Suits",
    cost=4,
    tags=[],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oceans, minimum=2, maximum=9
    ),
)
SatelliteFarms = GreenProjectCard(
    name="Satellite Farms",
    cost=17,
    tags=[Tag.Space],
)
Satellites = GreenProjectCard(
    name="Satellites",
    cost=14,
    tags=[Tag.Soace],
)
SlashAndBurnAgriculture = GreenProjectCard(
    name="Slash and Burn Agriculture",
    cost=8,
    tags=[Tag.Building],
    points=-1,
)
Smelting = GreenProjectCard(
    name="Smelting",
    cost=28,
    tags=[Tag.Building, Tag.Power],
)
SoilWarming = GreenProjectCard(
    name="Soil Warming",
    cost=24,
    tags=[Tag.Plant],
)
SolarPower = GreenProjectCard(
    name="Solar Power",
    cost=10,
    tags=[Tag.Building, Tag.Power],
    points=1,
)
SolarTrapping = GreenProjectCard(
    name="Solar Trapping",
    cost=10,
    tags=[Tag.Building],
)
Soletta = GreenProjectCard(
    name="Soletta",
    cost=30,
    tags=[Tag.Space],
    points=1,
)
SpaceHeaters = GreenProjectCard(
    name="Space Heaters",
    cost=11,
    tags=[Tag.Building],
)
SpaceStation = GreenProjectCard(
    name="Space Station",
    cost=14,
    tags=[Tag.Space],
    points=1,
)
Sponsors = GreenProjectCard(
    name="Sponsors",
    cost=5,
    tags=[Tag.Earth],
)
StripMine = GreenProjectCard(
    name="Strip Mine",
    cost=12,
    tags=[Tag.Building],
    requirements=GreenSpendRequirements(
        cost=1, req_type=SpendRequirementType.TerraformingRating
    ),
)
SurfaceMines = GreenProjectCard(
    name="Surface Mines",
    cost=13,
    tags=[Tag.Building],
)
TectonicStressPower = GreenProjectCard(
    name="Tectonic Stress Power",
    cost=20,
    tags=[Tag.Building, Tag.Power],
    points=1,
)
TitaniumMine = GreenProjectCard(
    name="Titanium Mine",
    cost=7,
    tags=[Tag.Building],
)
TollStation = GreenProjectCard(
    name="Toll Station",
    cost=16,
    tags=[],
)
TradingPost = GreenProjectCard(
    name="Trading Post",
    cost=11,
    tags=[],
)
TrappedHeat = GreenProjectCard(
    name="Trapped Heat",
    cost=20,
    tags=[],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
Trees = GreenProjectCard(
    name="Trees",
    cost=17,
    tags=[Tag.Plant],
    points=1,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Yellow,
        maxmium=GlobalParameterColor.White,
    ),
)
TropicalForest = GreenProjectCard(
    name="Tropical Forest",
    cost=19,
    tags=[],
    points=2,
    requirements=GreenSpendRequirements(cost=5, req_type=SpendRequirementType.Heat),
)
TundraFarming = GreenProjectCard(
    name="Tundra Farming",
    cost=12,
    tags=[Tag.Plant],
    points=1,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Temperature,
        minimum=GlobalParameterColor.Yellow,
        maximum=GlobalParameterColor.White,
    ),
)
UndergroundCity = GreenProjectCard(
    name="Underground City",
    cost=7,
    tags=[Tag.Building],
)
UnderseaVents = GreenProjectCard(
    name="Undersea Vents",
    cost=31,
    tags=[Tag.Building, Tag.Power],
)
VentureCapitalism = GreenProjectCard(
    name="Venture Capitalism",
    cost=11,
    tags=[],
)
WestaShipyard = GreenProjectCard(
    name="Westa Shipyard",
    cost=16,
    tags=[Tag.Building, Tag.Space, Tag.Jovian],
    points=1,
)
WavePower = GreenProjectCard(
    name="Wave Power",
    cost=9,
    tags=[Tag.Power],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oceans, minimum=3, maximum=9
    ),
)
Windmills = GreenProjectCard(
    name="Windmills",
    cost=10,
    tags=[Tag.Building, Tag.Power],
    points=1,
)
Worms = GreenProjectCard(
    name="Worms",
    cost=11,
    tags=[Tag.Microbe],
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
Zeppelins = GreenProjectCard(
    name="Zeppelins",
    cost=10,
    tags=[],
    points=1,
    requirements=GreenGlobalParameterRequirements(
        parameter_type=Oxygen,
        minimum=GlobalParameterColor.Red,
        maximum=GlobalParameterColor.White,
    ),
)
AssortedEnterprises = RedProjectCard(
    name="Assorted Enterprises",
    cost=2,
    tags=[Tag.Event],
)
CommercialImports = GreenProjectCard(
    name="Commercial Imports",
    cost=36,
    tags=[Tag.Space, Tag.Plant],
)
DiverseHabitats = GreenProjectCard(
    name="Diverse Habitats",
    cost=8,
    tags=[Tag.Plant],
)
FilterFeeders = BlueProjectCard(
    name="Filter Feeders",
    cost=9,
    tags=[Tag.Animal],
    points=None,
)
Laboratories = GreenProjectCard(
    name="Laboratories",
    cost=8,
    tags=[Tag.Science],
)
MatterGenerator = BlueProjectCard(
    name="Matter Generator",
    cost=13,
    tags=[Tag.Building, Tag.Power],
    action=MatterGeneratorAction(),
)
ProcessedMetals = GreenProjectCard(
    name="Processed Metals",
    cost=27,
    tags=[Tag.Space, Tag.Power],
    points=1,
)
ProcessingPlant = GreenProjectCard(
    name="Processing Plant",
    cost=19,
    tags=[Tag.Building, Tag.Power],
)
ProgressivePolicies = BlueProjectCard(
    name="Progressive Policies",
    cost=8,
    tags=[Tag.Science],
    action=ProgressivePoliciesAction(),
)
SyntheticCatastrophe = RedProjectCard(
    name="Synthetic Catastrophe",
    cost=0,
    tags=[Tag.Event],
)
SelfReplicatingBacteria = BlueProjectCard(
    name="Self-Replicating Bacteria",
    cost=8,
    tags=[Tag.Microbe],
    action=SelfReplicatingBacteriaAction(),
)

ALL_PROJECT_CARDS: list[ProjectCard] = [
    AdaptationTechnology,
    AdvancedAlloys,
    AdvancedScreeningTechnology,
    AiCentral,
    AnaerobicMicroorganisms,
    AntiGravityTechnology,
    AquiferPumping,
    ArcticAlgae,
    ArtificialJungle,
    AssemblyLines,
    AssetLiquidation,
    Birds,
    BrainstormingSession,
    CaretakerContract,
    CircuitBoardFactory,
    CommunityGardens,
    CompostingFactory,
    ConservedBiome,
    Decomposers,
    DecomposingFungus,
    DevelopedInfrastructure,
    DevelopmentCenter,
    EarthCatapult,
    EcologicalZone,
    EnergySubsidies,
    ExtendedResources,
    ExtremeColdFungus,
    FarmersMarket,
    FarmingCoOps,
    Fish,
    GHGProducingBacteria,
    Greenhouses,
    Herbivores,
    HydroElectricEnergy,
    InterplenetaryRelations,
    Interns,
    InterplanetaryConference,
    Ironworks,
    Livestock,
    MarsUniversity,
    MatterManufacturing,
    MediaGroup,
    NitriteReducingBacteria,
    OlympusConference,
    OptimalAerobraking,
    PhysicsComplex,
    PowerInfrastructure,
    RecycledDetritus,
    RedraftedContracts,
    RegolithEaters,
    ResearchOutpost,
    RestructuredResources,
    SmallAnimlas,
    Solarpunk,
    StandardTechnology,
    Steelworks,
    SymbioticFungus,
    Tardigrades,
    ThinkTank,
    UnitedPlanetaryAlliance,
    ViralEnhancers,
    VolcanicPools,
    WaterImportFromEuropa,
    WoodBurningStoves,
    AdvancedEcosystems,
    ArtificialLake,
    AtmosphereFiltering,
    BreathingFilters,
    BribedCommittee,
    BusinessContacts,
    CeoSFavoriteProject,
    ColonizerTrainingCamp,
    Comet,
    ConvoyFromEuropa,
    Crater,
    DeimosDown,
    GiantIceAsteroid,
    IceAsteroid,
    IceCapMelting,
    ImportedHydrogen,
    ImportedNitrogen,
    InterstellarColonuShip,
    InventionContest,
    InvestmentLoan,
    LagrangeObservatory,
    LakeMarineris,
    LargeConvoy,
    LavaFlows,
    LocalHeatTrapping,
    Mangrove,
    NitrogenRichAsteroid,
    PermafrostExtraction,
    PhobosFalls,
    Plantation,
    ReleaseOfInertGases,
    Research,
    SpecialDesign,
    SubterraneanReservoir,
    TechnologyDemonstration,
    TerraformingGanymede,
    TowingAComet,
    WorkCrews,
    AcquiredCompany,
    AdaptedLichen,
    AeratedMagma,
    AirborneRadiation,
    Algae,
    Archaebacteria,
    ArtificialPhotosynthesis,
    AsteroidMining,
    AsteroidMiningConsortium,
    Astrofarm,
    AtosphericInsulators,
    AutomatedFactories,
    BalancedPortfolios,
    BeamFromAThoriumAsteroid,
    BiomassCombustors,
    BiothermalPower,
    Blueprints,
    BuildingIndustries,
    Bushes,
    CallistoPenalMines,
    Cartel,
    CoalImports,
    CommercialDistrict,
    DeepWellHeating,
    DesignedMicroorganisms,
    DiversifiedInterests,
    DustyQuarry,
    EconomicGrowth,
    EnergyStorage,
    EosChasmaNationalPark,
    Farming,
    FoodFactory,
    FuelFactory,
    FueledGenerators,
    FusionPower,
    GanymedeShipyard,
    GeneRepair,
    GeothermalPower,
    GiantSpaceMirror,
    Grass,
    GreatDam,
    GreatEscarpmentConsortium,
    Heather,
    ImmigrationShuttles,
    ImportOfAdvancedGHG,
    ImportedGHG,
    IndustrialCenter,
    IndustiralFarming,
    IndustrialMicrobes,
    Insects,
    IoMiningIndustries,
    KelpFarming,
    Lichen,
    LightningHarvest,
    LowAtmoShields,
    LunarBeam,
    MassConverter,
    MedicalLab,
    MethaneFromTitan,
    MicroMills,
    Microprocessors,
    Mine,
    MirandaResort,
    MoholeArea,
    Monocultures,
    Moss,
    NaturalPreserve,
    NewPortfolios,
    NitrophilicMoss,
    NoctisFarming,
    NuclearPlants,
    PowerGrid,
    PowerPlant,
    PowerSupplyConsortium,
    ProtectedValley,
    QuantumExtractor,
    RadSuits,
    SatelliteFarms,
    Satellites,
    SlashAndBurnAgriculture,
    Smelting,
    SoilWarming,
    SolarPower,
    SolarTrapping,
    Soletta,
    SpaceHeaters,
    SpaceStation,
    Sponsors,
    StripMine,
    SurfaceMines,
    TectonicStressPower,
    TitaniumMine,
    TollStation,
    TradingPost,
    TrappedHeat,
    Trees,
    TropicalForest,
    TundraFarming,
    UndergroundCity,
    UnderseaVents,
    VentureCapitalism,
    WestaShipyard,
    WavePower,
    Windmills,
    Worms,
    Zeppelins,
    AssortedEnterprises,
    CommercialImports,
    DiverseHabitats,
    FilterFeeders,
    Laboratories,
    MatterGenerator,
    ProcessedMetals,
    ProcessingPlant,
    ProgressivePolicies,
    SyntheticCatastrophe,
    SelfReplicatingBacteria,
]
