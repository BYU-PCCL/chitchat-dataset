"""Simple unit tests for chitchat_dataset."""
import string

import chitchat_dataset as ccc

# TODO(mwilliammyers): add more/better tests  # noqa: W0511


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


class TestCompoundingConversationDataset:
    """Unit test for the CompoundingConversationDataset class."""

    def test_has_correct_length(self) -> None:
        """Tests that it has the correct length."""
        assert len(list(ccc.CompoundingConversationDataset())) == 131569


class TestMessageDataset:
    """Unit test for the MessageDataset class."""

    def test_has_correct_length(self) -> None:
        """Tests that it has the correct length."""
        assert len(list(ccc.MessageDataset())) == 138737


def test_compound_conversation() -> None:
    """Tests that it returns the correct length."""
    result = list(
        ccc.compound_conversation(
            list(string.ascii_lowercase),
            odd_speaker_token="1",
            even_speaker_token="2",
            prefix="",
        )
    )
    expected_result = [
        ("1a", "2b"),
        ("1a2b", "1c"),
        ("1a2b1c", "2d"),
        ("1a2b1c2d", "1e"),
        ("1a2b1c2d1e", "2f"),
        ("1a2b1c2d1e2f", "1g"),
        ("1a2b1c2d1e2f1g", "2h"),
        ("1a2b1c2d1e2f1g2h", "1i"),
        ("1a2b1c2d1e2f1g2h1i", "2j"),
        ("1a2b1c2d1e2f1g2h1i2j", "1k"),
        ("1a2b1c2d1e2f1g2h1i2j1k", "2l"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l", "1m"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m", "2n"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n", "1o"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o", "2p"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p", "1q"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p1q", "2r"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p1q2r", "1s"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p1q2r1s", "2t"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p1q2r1s2t", "1u"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p1q2r1s2t1u", "2v"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p1q2r1s2t1u2v", "1w"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p1q2r1s2t1u2v1w", "2x"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p1q2r1s2t1u2v1w2x", "1y"),
        ("1a2b1c2d1e2f1g2h1i2j1k2l1m2n1o2p1q2r1s2t1u2v1w2x1y", "2z"),
    ]
    assert len(result) == 25
    assert result == expected_result
