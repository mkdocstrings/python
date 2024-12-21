"""Snaphots for the inline-snapshot pytest plugin."""

from inline_snapshot import external, snapshot

snapshots_signatures = snapshot(
    {
        (
            ("separate_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("ccb0799542bf*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
        ): external("088cc77b47fe*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("3dfd0a4f1d56*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("bd8e85ddbdf2*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("16e25249d08a*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
        ): external("2bb0f7ef9acd*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("41139fbe91fd*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("059361c74a7b*.html"),
    }
)

snapshots_members = snapshot(
    {
        (
            ("filters", ("!a",)),
            ("inherited_members", ("a", "b")),
            ("members", ("a", "b")),
        ): external("1f91ad62b52c*.html"),
        (
            ("filters", ("!a",)),
            ("inherited_members", True),
            ("members", ("a", "b")),
        ): external("4cacea895bf1*.html"),
        (("filters", ()), ("inherited_members", False), ("members", False)): external(
            "d273600055bd*.html"
        ),
        (
            ("filters", ()),
            ("inherited_members", ("a", "b")),
            ("members", ("a", "b")),
        ): external("932e56579adc*.html"),
        (("filters", ("!a",)), ("inherited_members", ()), ("members", ())): external(
            "e01b6c847ee3*.html"
        ),
        (
            ("filters", None),
            ("inherited_members", True),
            ("members", ("a", "b")),
        ): external("ada31b59b5f3*.html"),
        (("filters", ("a",)), ("inherited_members", ()), ("members", True)): external(
            "b1e9cbeb30f5*.html"
        ),
        (
            ("filters", ()),
            ("inherited_members", ("a", "b")),
            ("members", None),
        ): external("2a0266e123ce*.html"),
        (
            ("filters", ("a",)),
            ("inherited_members", ("a", "b")),
            ("members", ("a", "b")),
        ): external("f5764202c23e*.html"),
        (
            ("filters", ("a",)),
            ("inherited_members", ("a", "b")),
            ("members", True),
        ): external("90429819e950*.html"),
        (
            ("filters", ("a",)),
            ("inherited_members", ()),
            ("members", ("a", "b")),
        ): external("1ab4cfefabc0*.html"),
        (("filters", None), ("inherited_members", ()), ("members", False)): external(
            "52f22ff10a8a*.html"
        ),
        (
            ("filters", None),
            ("inherited_members", ("a", "b")),
            ("members", None),
        ): external("293a35b887cf*.html"),
        (("filters", None), ("inherited_members", True), ("members", False)): external(
            "39e951487bdb*.html"
        ),
        (
            ("filters", None),
            ("inherited_members", ("a", "b")),
            ("members", False),
        ): external("edbbfef8a89b*.html"),
        (("filters", ("!a",)), ("inherited_members", ()), ("members", None)): external(
            "3bb0c857e1b7*.html"
        ),
        (("filters", ("a",)), ("inherited_members", False), ("members", ())): external(
            "08bbe49da00d*.html"
        ),
        (
            ("filters", ("!a",)),
            ("inherited_members", False),
            ("members", ("a", "b")),
        ): external("53ce3f6d8ac8*.html"),
        (("filters", ()), ("inherited_members", False), ("members", ())): external(
            "410ba8a168ff*.html"
        ),
        (
            ("filters", ("!a",)),
            ("inherited_members", ("a", "b")),
            ("members", None),
        ): external("96724a852648*.html"),
        (("filters", ("a",)), ("inherited_members", ()), ("members", False)): external(
            "d649cade214a*.html"
        ),
        (
            ("filters", ("a",)),
            ("inherited_members", ("a", "b")),
            ("members", None),
        ): external("361528c547e9*.html"),
        (
            ("filters", None),
            ("inherited_members", ("a", "b")),
            ("members", ()),
        ): external("3533b53bc483*.html"),
        (
            ("filters", ("!a",)),
            ("inherited_members", True),
            ("members", True),
        ): external("84d6099bfdb2*.html"),
        (
            ("filters", ("!a",)),
            ("inherited_members", ("a", "b")),
            ("members", True),
        ): external("5282625c5ef1*.html"),
        (("filters", None), ("inherited_members", ()), ("members", None)): external(
            "ff22bcb09c38*.html"
        ),
        (("filters", ("!a",)), ("inherited_members", True), ("members", ())): external(
            "2154fae6ed9a*.html"
        ),
        (
            ("filters", None),
            ("inherited_members", False),
            ("members", ("a", "b")),
        ): external("2e195fa646ee*.html"),
        (
            ("filters", None),
            ("inherited_members", ()),
            ("members", ("a", "b")),
        ): external("5e0bcd76595c*.html"),
        (
            ("filters", ("!a",)),
            ("inherited_members", True),
            ("members", None),
        ): external("c98383031472*.html"),
        (
            ("filters", ("a",)),
            ("inherited_members", True),
            ("members", False),
        ): external("b017c19d9ac0*.html"),
        (("filters", None), ("inherited_members", ()), ("members", True)): external(
            "8de05e82cb99*.html"
        ),
        (
            ("filters", None),
            ("inherited_members", ("a", "b")),
            ("members", True),
        ): external("fbef86b4c604*.html"),
        (("filters", ("!a",)), ("inherited_members", ()), ("members", False)): external(
            "8a7016b067da*.html"
        ),
        (("filters", ()), ("inherited_members", ()), ("members", True)): external(
            "ea6f9a89400d*.html"
        ),
        (
            ("filters", ("!a",)),
            ("inherited_members", False),
            ("members", False),
        ): external("827918d3dcfb*.html"),
        (
            ("filters", ()),
            ("inherited_members", False),
            ("members", ("a", "b")),
        ): external("32ac310bb4a9*.html"),
        (("filters", None), ("inherited_members", True), ("members", None)): external(
            "e6b47862501c*.html"
        ),
        (
            ("filters", ()),
            ("inherited_members", True),
            ("members", ("a", "b")),
        ): external("ddeb590e56cb*.html"),
        (
            ("filters", ("a",)),
            ("inherited_members", False),
            ("members", False),
        ): external("4975fdf8a5cf*.html"),
        (("filters", None), ("inherited_members", ()), ("members", ())): external(
            "a9852614c467*.html"
        ),
        (("filters", ("a",)), ("inherited_members", True), ("members", None)): external(
            "6ccdc50eac45*.html"
        ),
        (
            ("filters", None),
            ("inherited_members", ("a", "b")),
            ("members", ("a", "b")),
        ): external("a66759b8d926*.html"),
        (
            ("filters", ("a",)),
            ("inherited_members", False),
            ("members", True),
        ): external("d041b45b9ee4*.html"),
        (
            ("filters", ("a",)),
            ("inherited_members", True),
            ("members", ("a", "b")),
        ): external("0f219a1430d1*.html"),
        (("filters", ("a",)), ("inherited_members", ()), ("members", None)): external(
            "5cb33e97be1f*.html"
        ),
        (
            ("filters", ("!a",)),
            ("inherited_members", ("a", "b")),
            ("members", ()),
        ): external("8385c8f0906c*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("a", "b")),
            ("members", True),
        ): external("a4649ab17564*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", False)): external(
            "420f812dd0bd*.html"
        ),
        (("filters", None), ("inherited_members", False), ("members", ())): external(
            "71e5a7faa64e*.html"
        ),
        (
            ("filters", ("!a",)),
            ("inherited_members", False),
            ("members", True),
        ): external("43e849dfe137*.html"),
        (
            ("filters", ("a",)),
            ("inherited_members", False),
            ("members", ("a", "b")),
        ): external("d52dbf6ec43e*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("a", "b")),
            ("members", False),
        ): external("5578b36764ea*.html"),
        (("filters", None), ("inherited_members", True), ("members", ())): external(
            "e705bc6a2bf4*.html"
        ),
        (("filters", ()), ("inherited_members", False), ("members", None)): external(
            "a6418cfbd5cd*.html"
        ),
        (("filters", None), ("inherited_members", False), ("members", None)): external(
            "221d2fb12f69*.html"
        ),
        (
            ("filters", ("!a",)),
            ("inherited_members", ("a", "b")),
            ("members", False),
        ): external("b93ac88df469*.html"),
        (
            ("filters", ("!a",)),
            ("inherited_members", ()),
            ("members", ("a", "b")),
        ): external("4abe00bc3c9a*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", ("a", "b"))): external(
            "3fb232f78ae8*.html"
        ),
        (("filters", ()), ("inherited_members", ()), ("members", None)): external(
            "25cd0fb2669d*.html"
        ),
        (("filters", ("!a",)), ("inherited_members", ()), ("members", True)): external(
            "e93e076ba82a*.html"
        ),
        (("filters", ()), ("inherited_members", True), ("members", ())): external(
            "ac163ef952c9*.html"
        ),
        (("filters", ()), ("inherited_members", ("a", "b")), ("members", ())): external(
            "1af4b3b0865d*.html"
        ),
        (("filters", ()), ("inherited_members", False), ("members", True)): external(
            "351983452e01*.html"
        ),
        (("filters", ()), ("inherited_members", ()), ("members", ())): external(
            "418ee0b3df00*.html"
        ),
        (("filters", ()), ("inherited_members", True), ("members", False)): external(
            "b4625eea2521*.html"
        ),
        (("filters", None), ("inherited_members", False), ("members", True)): external(
            "83eb5f17a7f6*.html"
        ),
        (
            ("filters", ("!a",)),
            ("inherited_members", True),
            ("members", False),
        ): external("1af825b096ae*.html"),
        (("filters", ("a",)), ("inherited_members", True), ("members", True)): external(
            "540e98afb1d2*.html"
        ),
        (
            ("filters", ("a",)),
            ("inherited_members", ("a", "b")),
            ("members", False),
        ): external("3320be67ae6e*.html"),
        (("filters", ()), ("inherited_members", True), ("members", None)): external(
            "0811f7155ef5*.html"
        ),
        (
            ("filters", ("!a",)),
            ("inherited_members", False),
            ("members", None),
        ): external("3d6e64c1ca03*.html"),
        (
            ("filters", ("a",)),
            ("inherited_members", False),
            ("members", None),
        ): external("cb634eb46579*.html"),
        (("filters", ("a",)), ("inherited_members", True), ("members", ())): external(
            "5fbdd296af3a*.html"
        ),
        (("filters", ("a",)), ("inherited_members", ()), ("members", ())): external(
            "4c027d5be700*.html"
        ),
        (
            ("filters", ("a",)),
            ("inherited_members", ("a", "b")),
            ("members", ()),
        ): external("194588038e5b*.html"),
        (("filters", None), ("inherited_members", True), ("members", True)): external(
            "2bd1e859cd59*.html"
        ),
        (("filters", None), ("inherited_members", False), ("members", False)): external(
            "31e1fbb5ca91*.html"
        ),
        (("filters", ("!a",)), ("inherited_members", False), ("members", ())): external(
            "e9a1a8dd4f60*.html"
        ),
        (("filters", ()), ("inherited_members", True), ("members", True)): external(
            "7a390c841140*.html"
        ),
    }
)
