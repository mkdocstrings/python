"""Snaphots for the inline-snapshot pytest plugin."""

from inline_snapshot import external, snapshot

snapshots_signatures = snapshot(
    {
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("d03d16d1919a*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("e412376be64f*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("735fc6ffdb82*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("6a02b544c12c*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("b060b701543e*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
        ): external("74ee37cd1e94*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("4041a38e355f*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
        ): external("d1216ebf8e30*.html"),
    },
)

snapshots_members = snapshot(
    {
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("ab0ddac637b5*.html"),
        (("filters", None), ("inherited_members", True), ("members", True)): external("c0f102dbd7d4*.html"),
        (("filters", ()), ("inherited_members", False), ("members", True)): external("fca72854c849*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("6d12192d6b4d*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", False)): external("366b0537fe06*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("e90c3e0c85dd*.html"),
        (("filters", ()), ("inherited_members", True), ("members", True)): external("722165bce3ad*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("f8f32ea6a0c8*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("cd51e40cc0dd*.html"),
        (("filters", ()), ("inherited_members", False), ("members", False)): external("5cf0130e3b4f*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", True),
        ): external("34b16654e7ba*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", ()),
        ): external("fb5ebb7546d8*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("afd5c166367d*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("26bc66c2ba29*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("247a6063b698*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("5a9c10410801*.html"),
        (("filters", ()), ("inherited_members", False), ("members", ())): external("fba0d78ae23e*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("cfcd41685591*.html"),
        (("filters", ()), ("inherited_members", False), ("members", None)): external("eac5bee59a9e*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", False),
        ): external("76ee8e01e1c0*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("42c053a5e567*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("4f60da13e2d4*.html"),
        (("filters", ()), ("inherited_members", True), ("members", ())): external("c915eb92fd5d*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", None),
        ): external("c9a15552eed3*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("fe1cd23642d4*.html"),
        (("filters", None), ("inherited_members", False), ("members", False)): external("9bd282a6f2fe*.html"),
        (
            ("filters", None),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("166b8dfab738*.html"),
        (("filters", None), ("inherited_members", ()), ("members", False)): external("44e42f27bfe3*.html"),
        (("filters", None), ("inherited_members", False), ("members", None)): external("0f046dea611f*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", ()),
        ): external("28d8862dd086*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", False),
        ): external("f3f3acb6b51b*.html"),
        (("filters", None), ("inherited_members", ()), ("members", True)): external("dcf34c2f7269*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", None),
        ): external("8733f7fb7b6d*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", False),
        ): external("eee65d3705a6*.html"),
        (
            ("filters", None),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("a200913d9a7d*.html"),
        (
            ("filters", None),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("bd6594ae3b51*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("8d4e1f9af997*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", ()),
        ): external("d5a6bf59c663*.html"),
        (("filters", None), ("inherited_members", ()), ("members", None)): external("fd291f98ca28*.html"),
        (("filters", ()), ("inherited_members", True), ("members", None)): external("14bca0e5703b*.html"),
        (
            ("filters", ()),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("09d96d69d9dc*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("43d819f94dc7*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", ()),
        ): external("95f8e480937f*.html"),
        (("filters", None), ("inherited_members", False), ("members", True)): external("f4150843096a*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", True),
        ): external("3c21330afd65*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", None),
        ): external("d55652702606*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("f0014d9505ec*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("96cf94f4822a*.html"),
        (("filters", None), ("inherited_members", True), ("members", ())): external("ce06da7f07b3*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", False),
        ): external("74bfab19cbd4*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("75b69b702f3b*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", False),
        ): external("d726cb8367d9*.html"),
        (("filters", None), ("inherited_members", False), ("members", ())): external("fb770e6537bc*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", None),
        ): external("2bf34b4dd82e*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("4892e0fe1920*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", True),
        ): external("13334b5b4fcf*.html"),
        (
            ("filters", ()),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("388a13d71284*.html"),
        (("filters", None), ("inherited_members", True), ("members", False)): external("3f5d794823a4*.html"),
        (
            ("filters", ()),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("9d03089a46fa*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("8b097c69ac2f*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", True),
        ): external("cd3e45851714*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("e3defc3620e5*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", True),
        ): external("84193b3c9f5d*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("c6e7ef9564cd*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", None),
        ): external("62e18d3e5777*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", None),
        ): external("3935bcf6d71b*.html"),
        (("filters", None), ("inherited_members", ()), ("members", ())): external("f77f1c850398*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", True),
        ): external("fe25ab760039*.html"),
        (("filters", None), ("inherited_members", True), ("members", None)): external("ea914f1afa9d*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", None)): external("19f98a747c01*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", ()),
        ): external("c260e7f4ef3b*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("9720526cf5e4*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("f6e292b8358a*.html"),
        (("filters", ()), ("inherited_members", True), ("members", False)): external("b0a9b08f1f72*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", True)): external("027ef7afeffc*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", False),
        ): external("710706687213*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", ())): external("11598fec2d07*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("e8608b0de174*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("e5dc372374af*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", ()),
        ): external("a185e216dc7b*.html"),
        (("filters", "public"), ("inherited_members", ("method1",)), ("members", None)): external("6af55596d9c4*.html"),
        (("filters", "public"), ("inherited_members", ("method1",)), ("members", False)): external(
            "6abf5ddd819b*.html",
        ),
        (("filters", "public"), ("inherited_members", ()), ("members", None)): external("6d72c524b827*.html"),
        (("filters", "public"), ("inherited_members", False), ("members", False)): external("9dab67183389*.html"),
        (("filters", "public"), ("inherited_members", ("method1",)), ("members", True)): external("6c0b7207df03*.html"),
        (("filters", "public"), ("inherited_members", True), ("members", ())): external("f48d651b3f1a*.html"),
        (("filters", "public"), ("inherited_members", ("method1",)), ("members", ("module_attribute",))): external(
            "408244423577*.html",
        ),
        (("filters", "public"), ("inherited_members", True), ("members", None)): external("16295fa51a2c*.html"),
        (("filters", "public"), ("inherited_members", True), ("members", True)): external("37232379c426*.html"),
        (("filters", "public"), ("inherited_members", ()), ("members", ())): external("2e866eca9a45*.html"),
        (("filters", "public"), ("inherited_members", True), ("members", False)): external("ed5d07bcdbaa*.html"),
        (("filters", "public"), ("inherited_members", False), ("members", ())): external("135f57223e00*.html"),
        (("filters", "public"), ("inherited_members", False), ("members", None)): external("b4e20d5cd52e*.html"),
        (("filters", "public"), ("inherited_members", ()), ("members", False)): external("46daa7e60b98*.html"),
        (("filters", "public"), ("inherited_members", False), ("members", True)): external("a255ee80bf7a*.html"),
        (("filters", "public"), ("inherited_members", ()), ("members", True)): external("74e2496015e1*.html"),
        (("filters", "public"), ("inherited_members", True), ("members", ("module_attribute",))): external(
            "e254ae60f9af*.html",
        ),
        (("filters", "public"), ("inherited_members", ("method1",)), ("members", ())): external("51d73351dc55*.html"),
        (("filters", "public"), ("inherited_members", ()), ("members", ("module_attribute",))): external(
            "d56d3aeae22b*.html",
        ),
        (("filters", "public"), ("inherited_members", False), ("members", ("module_attribute",))): external(
            "80399c502938*.html",
        ),
        (("heading", ""), ("members", False), ("separate_signature", False), ("show_if_no_docstring", True)): external(
            "d1dd339f9260*.html",
        ),
        (
            ("heading", "Some heading"),
            ("members", False),
            ("separate_signature", True),
            ("show_if_no_docstring", True),
        ): external("480324b25439*.html"),
        (("heading", ""), ("members", False), ("separate_signature", True), ("show_if_no_docstring", True)): external(
            "2eef87791b97*.html",
        ),
        (
            ("heading", "Some heading"),
            ("members", False),
            ("separate_signature", False),
            ("show_if_no_docstring", True),
        ): external("51deee0f00f3*.html"),
    },
)
