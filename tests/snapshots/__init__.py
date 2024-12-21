"""Snaphots for the inline-snapshot pytest plugin."""

from inline_snapshot import external, snapshot

snapshots_signatures = snapshot(
    {
        (
            ("separate_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("bdccb1c54ddb*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
        ): external("4172790fb395*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("1ad4856d25ba*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("fddc58e74a8d*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("eb5c12af04ce*.html"),
        (
            ("separate_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
        ): external("b76508c45ed5*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("a2cc94940288*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("2fa0d152e802*.html"),
    },
)

snapshots_members = snapshot(
    {
        (("filters", ()), ("inherited_members", False), ("members", False)): external(
            "d273600055bd*.html",
        ),
        (("filters", None), ("inherited_members", ()), ("members", False)): external(
            "52f22ff10a8a*.html",
        ),
        (("filters", None), ("inherited_members", True), ("members", False)): external(
            "39e951487bdb*.html",
        ),
        (("filters", ()), ("inherited_members", False), ("members", ())): external(
            "410ba8a168ff*.html",
        ),
        (("filters", None), ("inherited_members", ()), ("members", None)): external(
            "decb32481637*.html",
        ),
        (("filters", None), ("inherited_members", ()), ("members", True)): external(
            "d6c8fac31f3d*.html",
        ),
        (("filters", ()), ("inherited_members", ()), ("members", True)): external(
            "9215ddeecefe*.html",
        ),
        (("filters", None), ("inherited_members", True), ("members", None)): external(
            "30b20db3fbb6*.html",
        ),
        (("filters", None), ("inherited_members", ()), ("members", ())): external(
            "a9852614c467*.html",
        ),
        (("filters", ()), ("inherited_members", ()), ("members", False)): external(
            "420f812dd0bd*.html",
        ),
        (("filters", None), ("inherited_members", False), ("members", ())): external(
            "71e5a7faa64e*.html",
        ),
        (("filters", None), ("inherited_members", True), ("members", ())): external(
            "e705bc6a2bf4*.html",
        ),
        (("filters", ()), ("inherited_members", False), ("members", None)): external(
            "4cbaa8693392*.html",
        ),
        (("filters", None), ("inherited_members", False), ("members", None)): external(
            "514472f7d620*.html",
        ),
        (("filters", ()), ("inherited_members", ()), ("members", None)): external(
            "c958f0f2c735*.html",
        ),
        (("filters", ()), ("inherited_members", True), ("members", ())): external(
            "ac163ef952c9*.html",
        ),
        (("filters", ()), ("inherited_members", False), ("members", True)): external(
            "0896812735b0*.html",
        ),
        (("filters", ()), ("inherited_members", ()), ("members", ())): external(
            "418ee0b3df00*.html",
        ),
        (("filters", ()), ("inherited_members", True), ("members", False)): external(
            "b4625eea2521*.html",
        ),
        (("filters", None), ("inherited_members", False), ("members", True)): external(
            "fd9bc4ba54f6*.html",
        ),
        (("filters", ()), ("inherited_members", True), ("members", None)): external(
            "d1ebaf56f232*.html",
        ),
        (("filters", None), ("inherited_members", True), ("members", True)): external(
            "1c028c256532*.html",
        ),
        (("filters", None), ("inherited_members", False), ("members", False)): external(
            "31e1fbb5ca91*.html",
        ),
        (("filters", ()), ("inherited_members", True), ("members", True)): external(
            "264eeab98d34*.html",
        ),
    },
)
