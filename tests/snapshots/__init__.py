"""Snaphots for the inline-snapshot pytest plugin."""

from inline_snapshot import external, snapshot

snapshots_signatures = snapshot(
    {
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("4370d843cc76*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("955e5111f426*.html"),
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
        ): external("f5ce06acbb7a*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("9c0bfc0ee407*.html"),
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
        (("filters", None), ("inherited_members", True), ("members", True)): external(
            "0b1372d7f7c0*.html",
        ),
        (("filters", ()), ("inherited_members", False), ("members", True)): external(
            "59a9e1ffb2f0*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("6d12192d6b4d*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", False)): external(
            "366b0537fe06*.html",
        ),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("e90c3e0c85dd*.html"),
        (("filters", ()), ("inherited_members", True), ("members", True)): external(
            "e8be7a9b1410*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("f8f32ea6a0c8*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("d540895f6bf9*.html"),
        (("filters", ()), ("inherited_members", False), ("members", False)): external(
            "5cf0130e3b4f*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", True),
        ): external("7c988c9e13ef*.html"),
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
        (("filters", ()), ("inherited_members", False), ("members", ())): external(
            "fba0d78ae23e*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("cfcd41685591*.html"),
        (("filters", ()), ("inherited_members", False), ("members", None)): external(
            "a2c5be9bd5d1*.html",
        ),
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
        (("filters", ()), ("inherited_members", True), ("members", ())): external(
            "c915eb92fd5d*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", None),
        ): external("c9a15552eed3*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("3d072a22b951*.html"),
        (("filters", None), ("inherited_members", False), ("members", False)): external(
            "9bd282a6f2fe*.html",
        ),
        (
            ("filters", None),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("166b8dfab738*.html"),
        (("filters", None), ("inherited_members", ()), ("members", False)): external(
            "44e42f27bfe3*.html",
        ),
        (("filters", None), ("inherited_members", False), ("members", None)): external(
            "f7711b8af768*.html",
        ),
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
        (("filters", None), ("inherited_members", ()), ("members", True)): external(
            "347d4ffe2cb3*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", None),
        ): external("ba51e100acd4*.html"),
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
        (("filters", None), ("inherited_members", ()), ("members", None)): external(
            "88855b028417*.html",
        ),
        (("filters", ()), ("inherited_members", True), ("members", None)): external(
            "981438492e38*.html",
        ),
        (
            ("filters", ()),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("09d96d69d9dc*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("ae74b5980f9b*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", ()),
        ): external("95f8e480937f*.html"),
        (("filters", None), ("inherited_members", False), ("members", True)): external(
            "831198033381*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", True),
        ): external("052c34f22e4c*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", None),
        ): external("cdc8126d78b6*.html"),
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
        (("filters", None), ("inherited_members", True), ("members", ())): external(
            "ce06da7f07b3*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", False),
        ): external("74bfab19cbd4*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("7d5fe6653919*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", False),
        ): external("d726cb8367d9*.html"),
        (("filters", None), ("inherited_members", False), ("members", ())): external(
            "fb770e6537bc*.html",
        ),
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
        ): external("46e56f39b10d*.html"),
        (
            ("filters", ()),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("388a13d71284*.html"),
        (("filters", None), ("inherited_members", True), ("members", False)): external(
            "3f5d794823a4*.html",
        ),
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
        ): external("052e71e7e9d5*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("e3defc3620e5*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", True),
        ): external("b4b490164ab1*.html"),
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
        ): external("728c13446301*.html"),
        (("filters", None), ("inherited_members", ()), ("members", ())): external(
            "f77f1c850398*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", True),
        ): external("0fac4f5e7f45*.html"),
        (("filters", None), ("inherited_members", True), ("members", None)): external(
            "cc19537fdba4*.html",
        ),
        (("filters", ()), ("inherited_members", ()), ("members", None)): external(
            "e6a9b76f268c*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", ()),
        ): external("c260e7f4ef3b*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("0c2924ff976f*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("f6e292b8358a*.html"),
        (("filters", ()), ("inherited_members", True), ("members", False)): external(
            "b0a9b08f1f72*.html",
        ),
        (("filters", ()), ("inherited_members", ()), ("members", True)): external(
            "fb65efbbfc3e*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", False),
        ): external("710706687213*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", ())): external(
            "11598fec2d07*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("a1167b14f5a7*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("f848d4a9e516*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", ()),
        ): external("a185e216dc7b*.html"),
    },
)
