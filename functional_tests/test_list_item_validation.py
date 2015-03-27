from .base import FunctionalTest

class ListValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box

        # The home page refreshes and there is an error message saying
        # that list items cannot be blank

        # She tres again with some text for the item, which now works

        # Perversly, she now attempts to submit another blank item

        # She receives simlar message on the list page

        # And she can correct it by filling some text in
        self.fail("Write me!")
