from abc import abstractmethod, ABC
from typing import List, Type, Union

from .enums import Phase, SpendRequirementType, Tag
from .global_requirements import GlobalParameterColor, GlobalParameter
from .player import Player


class CardRequirements(ABC):
    def meets_conditions(self, player: Player) -> bool:
        return self._meets_color_conditions(player) and self._meets_custom_conditions(player)

    @abstractmethod
    def _meets_color_conditions(self, player: Player) -> bool:
        raise NotImplementedError

    @abstractmethod
    def _meets_custom_conditions(self, player: Player) -> bool:
        raise NotImplementedError

class GreenCardRequirements(CardRequirements, ABC):
    def _meets_color_conditions(self, player: Player) -> bool:
        return player.game.get_current_phase() == Phase.Development and not player.has_played_green_card


class RedBlueCardRequirements(CardRequirements, ABC):
    def _meets_color_conditions(self, player: Player) -> bool:
        return player.game.get_current_phase() == Phase.Construction \
               and (not player.has_played_red_or_blue_card
                    or player.is_eligible_for_bonus(Phase.Construction))


class DefaultGreenCardRequirements(GreenCardRequirements):
    def _meets_custom_conditions(self, player: Player) -> bool:
        return True


class DefaultRedBlueCardRequirements(RedBlueCardRequirements):
    def _meets_custom_conditions(self, player: Player) -> bool:
        return True


class GlobalParameterRequirements(CardRequirements, ABC):
    def __init__(self, minimum: Union[int, GlobalParameterColor], maximum: Union[int, GlobalParameterColor], parameter_type: Type[GlobalParameter]):
        self.minimum = minimum
        self.maximum = maximum
        self.parameter_type = parameter_type

    def _meets_custom_conditions(self, player: Player) -> bool:
        return self.minimum <= player.game.global_requirements.current_value(self.parameter_type) <= self.maximum

class GreenGlobalParameterRequirements(GlobalParameterRequirements, GreenCardRequirements):
    pass


class RedBlueGlobalParameterRequirements(GlobalParameterRequirements, RedBlueCardRequirements):
    pass


class TagRequirements(CardRequirements, ABC):
    def __init__(self, minimum: int, tag: Tag):
        self.minimum = minimum
        self.tag = tag

    def _meets_custom_conditions(self, player: Player) -> bool:
        return self.minimum <= len([card for card in player.played_project_cards if self.tag in card.tags])

class GreenTagRequirements(TagRequirements, GreenCardRequirements):
    pass


class RedBlueTagRequirements(TagRequirements, RedBlueCardRequirements):
    pass


class SpendRequirements(CardRequirements, ABC):
    # TODO: Come up with a cleaner way to handle the *one* card where
    #       you don't actually need to spend the cost, and just need it.
    #       Probably want a separate parent class.
    def __init__(self, cost: int, req_type: SpendRequirementType, spend=True):
        self.cost = cost
        self.req_type = req_type
        self.spend = spend

    def _meets_custom_conditions(self, player: Player) -> bool:
        if self.req_type == SpendRequirementType.TerraformingRating:
            current_value = player.terraforming_rating
        else:
            current_value = getattr(player.board, self.req_type.name.lower())
        return self.cost <= current_value

class GreenSpendRequirements(SpendRequirements, GreenCardRequirements):
    pass


class RedBlueSpendRequirements(SpendRequirements, RedBlueCardRequirements):
    pass


class CardRequirementsUnion(CardRequirements):
    def __init__(self, *args: List[CardRequirements]):
        self.children = args

    def meets_conditions(self, player: Player) -> bool:
        return all(child.meets_conditions(player) for child in self.children)
