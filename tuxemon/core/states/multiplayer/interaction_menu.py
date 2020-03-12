from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from tuxemon.core.menu.interface import MenuItem
from tuxemon.core.menu.menu import PopUpMenu


class InteractionMenu(PopUpMenu):
    def initialize_items(self):
        def duel():
            self.session.wants_duel = True

        def trade():
            pass

        kwagrs = {
            "accept", duel,
            "decline", self.session.pop_state
        }
        kwagrs = {
            "accept", trade,
            "decline", self.session.pop_state
        }

        # if self.session.game.isclient or self.session.game.ishost:
        #    self.session.game.client.player_interact(self.player, "DUEL")
        # self.session.game.client.player_interact(self.player, self.interaction, "CLIENT_RESPONSE", response)


class ConfirmMenu(PopUpMenu):
    def startup(self, **kwargs):
        super(ConfirmMenu, self).startup(**kwargs)
        self.item_to_use = kwargs["item"]

    def calc_final_rect(self):
        rect = self.rect.copy()
        rect.width *= .25
        rect.height *= .3
        rect.center = self.rect.center
        return rect

    def use_selected_item(self):
        item = self.get_selected_item().game_object

        # TODO: combat checks?

        player = self.session.player
        item.use(player, self.session)

    def initialize_items(self):
        menu_items_map = (
            ('ACCEPT', self.accept),
            ('DECLINE', self.decline),
        )

        for label, callback in menu_items_map:
            image = self.shadow_text(label)
            item = MenuItem(image, label, None, None, callback)
            self.add(item)
