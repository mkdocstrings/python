"""Snaphots for the inline-snapshot pytest plugin."""

from inline_snapshot import external, snapshot

snapshots_signatures = snapshot(
    {
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("5a81bf8d075a*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
        ): external("4b44c8524385*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
        ): external("ce6f9af785a3*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("404ebda5daa1*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("60692fbc929d*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("f0be8c48bdb1*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("77ef7df64794*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("ea97f7d3bbb8*.html"),
    },
)

snapshots_members = snapshot(
    {
        (
            ("filters", ()),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("8b6a7773eeda*.html"),
        (("filters", ()), ("inherited_members", False), ("members", False)): external(
            "526f9769a8d8*.html",
        ),
        (("filters", ()), ("inherited_members", ()), ("members", ())): external(
            "1a62cc2a6348*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", False),
        ): external("61d7cd63d924*.html"),
        (("filters", None), ("inherited_members", False), ("members", False)): external(
            "034b4efd3e13*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", False),
        ): external("91bff55e26ac*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("bc1041795f2d*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("69430148d9bd*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", True),
        ): external("955f3255e376*.html"),
        (("filters", ()), ("inherited_members", False), ("members", True)): external(
            "7e57f525a5cf*.html",
        ),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("c2d169fd563f*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("4742b8716333*.html"),
        (("filters", ()), ("inherited_members", True), ("members", ())): external(
            "8fcb2a1de876*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("b2438d1195bd*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("89b2703bc063*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("dd2fe557b7a7*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("80796d270928*.html"),
        (
            ("filters", ()),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("5f72a3efb2a0*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", False),
        ): external("526cde6c077e*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", True),
        ): external("0b78bd712192*.html"),
        (("filters", ()), ("inherited_members", False), ("members", None)): external(
            "fb9e57ae5121*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", False),
        ): external("5dd25fa89bcf*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("d74b55f548b0*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("120c39cfb973*.html"),
        (("filters", ()), ("inherited_members", True), ("members", None)): external(
            "04cf3d5c7895*.html",
        ),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("2bb9dcc2e619*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", False),
        ): external("95b7e6fc3fae*.html"),
        (("filters", None), ("inherited_members", True), ("members", None)): external(
            "c772a3a790f9*.html",
        ),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("8054d8ab1742*.html"),
        (("filters", None), ("inherited_members", ()), ("members", False)): external(
            "5765a59f2465*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("f381581054e5*.html"),
        (("filters", ()), ("inherited_members", False), ("members", ())): external(
            "b6a3e548f8a7*.html",
        ),
        (("filters", None), ("inherited_members", ()), ("members", True)): external(
            "b081434f8084*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("e9bfa116c60f*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", None),
        ): external("9931367ff76d*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("f6889768add4*.html"),
        (("filters", None), ("inherited_members", ()), ("members", None)): external(
            "98164d145261*.html",
        ),
        (("filters", ()), ("inherited_members", ()), ("members", False)): external(
            "510920fc9f8a*.html",
        ),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("c4287b327f2f*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("8b3cb3a9393b*.html"),
        (
            ("filters", None),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("3eae6454c5cd*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", None),
        ): external("0917f5f8089a*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("37aba2e60532*.html"),
        (("filters", ()), ("inherited_members", True), ("members", False)): external(
            "602be277ba8b*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", True),
        ): external("40db9513bd7d*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("cb9f37ea6df7*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("e0a486cfc020*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", ()),
        ): external("bc9991f6f692*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("2db574c46878*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", ()),
        ): external("4c974305bdd0*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("e4835b75b42e*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("9ac92fafd7c5*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", None),
        ): external("103c4e100ff0*.html"),
        (("filters", None), ("inherited_members", False), ("members", True)): external(
            "0fca514fd462*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", ()),
        ): external("ec2b4bcdfdd7*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("a1a44b6963ee*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", True)): external(
            "49e01ef023a5*.html",
        ),
        (
            ("filters", ()),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("ca6eeb7fde7c*.html"),
        (
            ("filters", None),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("fea4b8369aea*.html"),
        (("filters", None), ("inherited_members", True), ("members", ())): external(
            "cc7645e3f794*.html",
        ),
        (("filters", None), ("inherited_members", False), ("members", None)): external(
            "f1da2be691e0*.html",
        ),
        (("filters", None), ("inherited_members", False), ("members", ())): external(
            "158c9a6f19ce*.html",
        ),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("064454f2c4bd*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("dda6dce2c75e*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", None)): external(
            "8561527abb31*.html",
        ),
        (
            ("filters", None),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("5b95dcb05554*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", ()),
        ): external("54b775cb4537*.html"),
        (("filters", ()), ("inherited_members", True), ("members", True)): external(
            "eff41840b867*.html",
        ),
        (("filters", None), ("inherited_members", ()), ("members", ())): external(
            "966774acc7af*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", ()),
        ): external("495b3a54efd8*.html"),
        (("filters", None), ("inherited_members", True), ("members", False)): external(
            "2a58672fcba8*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", None),
        ): external("6ff3c37b8792*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", None),
        ): external("ead01120c355*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", ()),
        ): external("894037f2c998*.html"),
        (("filters", None), ("inherited_members", True), ("members", True)): external(
            "83da7d2d8821*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", True),
        ): external("b47fe5c72b71*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", True),
        ): external("6adfcb72f936*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", None),
        ): external("423e03090516*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", True),
        ): external("376dfb4b9fc9*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", False),
        ): external("97051ae4cc47*.html"),
    },
)
