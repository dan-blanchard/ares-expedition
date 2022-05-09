from .action import Action
from .enums import Phase, Tag
from .global_requirements import Oceans, Oxygen
from .player import Player



class SteelworksAction(Action):
    def play(self, player: Player) -> None:
        player.board.remove_heat(6)
        player.board.add_megacredits(2)
        player.increase_global_parameter(Oxygen)

    def meets_conditions(self, player: Player) -> bool:
        return player.board.heat >= 6


class CommunityGardensAction(Action):
    def play(self, player: Player) -> None:
        player.board.add_megacredits(2)
        if player.current_phase_card == Phase.Action:
            player.board.add_plants(1)

    def meets_conditions(self, player: Player) -> bool:
        return True


class WaterImportFromEuropaAction(Action):
    def get_cost(self, player: Player) -> int:
        return max(0, 12 - player.board.production_titanium)

    def meets_conditions(self, player: Player) -> bool:
        return player.board.megacredits >= self.get_cost(player)

    def play(self, player: Player) -> None:
        player.board.remove_megacredits(self.get_cost(player))
        player.increase_global_parameter(Oceans)


class AdvancedScreeningTechnologyAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class AICentralAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class AquiferPumpingAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class ArtificialJungleAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class AssetLiquidationAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class BirdsAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class BrainstormingSessionAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class CaretakerContractAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class CircuitBoardFactoryAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class ConservedBiomeAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class DecomposingFungusAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class DevelopedInfrastructureAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class DevelopmentCenterAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class ExtremeColdFungusAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class FarmersMarketAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class FarmingCoOpsAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class GHGProducingBacteriaAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class GreenhousesAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class HydroElectricEnergyAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class IronworksAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class MatterManufacturingAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class NitriteReducingBacteriaAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class PowerInfrastructureAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class RedraftedContractsAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class RegolithEatersAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class SolarpunkAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class SymbioticFungusAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class ThinkTankAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class VolcanicPoolsAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class WoodBurningStovesAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class MatterGeneratorAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class ProgressivePoliciesAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()

class SelfReplicatingBacteriaAction(Action):
    def meets_conditions(self, player: Player) -> bool:
        raise NotImplementedError()

    def play(self, player: Player) -> None:
        raise NotImplementedError()
