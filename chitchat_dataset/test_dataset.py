"""Simple unit tests for chitchat_dataset."""
import chitchat_dataset as ccc


class TestDataset:
    """Unit test for the Dataset class."""

    _dataset = ccc.Dataset()

    def test_has_correct_length(self) -> None:
        """Tests that it has the correct length."""
        assert len(list(self._dataset)) == 7168

    def test_has_approx_correct_order(self) -> None:
        """Tests that it in approximately the correct order."""
        keys = list(self._dataset.keys())

        assert keys[0] == "a07edb12-6b91-4138-b11e-02421888d699"
        assert keys[7167] == "adac5dae-e2df-4701-a0fc-d5feaedac7b1"
        # these indices were randomly chosen from a uniform distribution
        assert keys[19] == "b081fda7-d422-432c-82b4-003377df5103"
        assert keys[4642] == "b33257fd-ab2c-4d38-a524-a67553d0c467"
        assert keys[4347] == "84646024-a21d-48e7-8678-3533b3fe8493"
        assert keys[656] == "ffb695f6-3ae9-4455-b5af-f3b1bbc9db4a"
        assert keys[4695] == "62cc0122-1ba8-4d53-b28c-5c2123514e85"
        assert keys[2491] == "5be70320-0a13-4e58-b069-e6e840d9c262"
        assert keys[227] == "5b7aafb1-669c-47ea-b84e-bc61f5ca9f15"
        assert keys[755] == "a680f047-38fa-4201-955f-7fbe7577d826"
        assert keys[4706] == "ce48a727-0f9c-4c8a-beee-a939ce8cec90"
        assert keys[957] == "d4286b1c-1c2d-4d1c-875e-1a09c18175e2"


class TestConversationDataset:
    """Unit test for the ConversationDataset class."""

    def test_has_correct_length(self) -> None:
        """Tests that it has the correct length."""
        assert len(list(ccc.ConversationDataset())) == 7168


class TestMessageDataset:
    """Unit test for the MessageDataset class."""

    def test_has_correct_length(self) -> None:
        """Tests that it has the correct length."""
        assert len(list(ccc.MessageDataset())) == 138737
