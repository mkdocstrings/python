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
            ("signature_crossrefs", True),
        ): external("2fa0d152e802*.html"),
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
            ("separate_signature", False),
            ("show_signature_annotations", True),
            ("signature_crossrefs", True),
        ): external("fddc58e74a8d*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", True),
            ("signature_crossrefs", False),
        ): external("4172790fb395*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", True),
        ): external("a2cc94940288*.html"),
        (
            ("separate_signature", True),
            ("show_signature_annotations", False),
            ("signature_crossrefs", False),
        ): external("1ad4856d25ba*.html"),
    },
)

snapshots_members = snapshot(
    {
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", ()),
        ): external("3d5810bf108d*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", None)): external(
            "c958f0f2c735*.html",
        ),
        (("filters", ()), ("inherited_members", True), ("members", True)): external(
            "264eeab98d34*.html",
        ),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("92caf0644088*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("cc79a0b4f0bd*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("c2ae9d2ec008*.html"),
        (("filters", None), ("inherited_members", False), ("members", ())): external(
            "71e5a7faa64e*.html",
        ),
        (("filters", ()), ("inherited_members", ()), ("members", True)): external(
            "9215ddeecefe*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("19e32cf4fe5c*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("65d6167f9d56*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("df7108ee046c*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", ())): external(
            "418ee0b3df00*.html",
        ),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("54fc28f8c950*.html"),
        (
            ("filters", ()),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("7056622b66ca*.html"),
        (("filters", None), ("inherited_members", ()), ("members", ())): external(
            "a9852614c467*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", False),
        ): external("325879abca0c*.html"),
        (("filters", ()), ("inherited_members", False), ("members", ())): external(
            "410ba8a168ff*.html",
        ),
        (
            ("filters", None),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("4a963879599c*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("ff19b1bb907d*.html"),
        (("filters", ()), ("inherited_members", ()), ("members", False)): external(
            "420f812dd0bd*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", ()),
        ): external("e6d10fc6f7c5*.html"),
        (("filters", None), ("inherited_members", False), ("members", None)): external(
            "514472f7d620*.html",
        ),
        (("filters", None), ("inherited_members", False), ("members", False)): external(
            "31e1fbb5ca91*.html",
        ),
        (("filters", None), ("inherited_members", True), ("members", False)): external(
            "39e951487bdb*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", None),
        ): external("579a9625e955*.html"),
        (("filters", None), ("inherited_members", True), ("members", None)): external(
            "30b20db3fbb6*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", ()),
        ): external("7f0065cc9f63*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("7e8151d6fac2*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("0fff1a95a5de*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", ()),
        ): external("ae6f307ff315*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("c136077acda2*.html"),
        (("filters", None), ("inherited_members", True), ("members", True)): external(
            "1c028c256532*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", None),
        ): external("19319e59121c*.html"),
        (("filters", ()), ("inherited_members", False), ("members", False)): external(
            "d273600055bd*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", False),
        ): external("3e82ec3e444a*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", False),
        ): external("97bf952fd6e7*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", True),
        ): external("5ce5c3a9c44b*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("6bfd855dedf9*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", True),
        ): external("037890114186*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("95d9eb7e4814*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("f08d0ebb542c*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", None),
        ): external("0d3b3555dfd4*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", True),
        ): external("7c62021f9ce2*.html"),
        (("filters", ()), ("inherited_members", True), ("members", False)): external(
            "b4625eea2521*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("5c041919edbf*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("26962d0cb5a1*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", ()),
        ): external("c49089ed5bd4*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", True),
        ): external("9c2ca22b6919*.html"),
        (
            ("filters", ()),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("7dcbecc97d40*.html"),
        (
            ("filters", None),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("a5b7b1963442*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("d24bf1894f7b*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", ("module_attribute",)),
        ): external("5b1f74a102a8*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("7ecf729ccd51*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ()),
            ("members", None),
        ): external("0577775bbb17*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", True),
        ): external("a2e7f5c3beba*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("d117610f9230*.html"),
        (
            ("filters", None),
            ("inherited_members", ("method1",)),
            ("members", None),
        ): external("51273305ce1e*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", False),
        ): external("869ebc3be682*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", True),
            ("members", None),
        ): external("ad31ef6fe974*.html"),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", True),
        ): external("1e87360a9e21*.html"),
        (("filters", None), ("inherited_members", ()), ("members", True)): external(
            "d6c8fac31f3d*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", ()),
        ): external("bcdb51311acc*.html"),
        (("filters", ()), ("inherited_members", True), ("members", ())): external(
            "ac163ef952c9*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", None),
        ): external("919be399f0d7*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", False),
            ("members", False),
        ): external("850a84590343*.html"),
        (("filters", ()), ("inherited_members", True), ("members", None)): external(
            "d1ebaf56f232*.html",
        ),
        (
            ("filters", ("module_attribute",)),
            ("inherited_members", False),
            ("members", False),
        ): external("3e9d3c783d98*.html"),
        (("filters", ()), ("inherited_members", False), ("members", None)): external(
            "4cbaa8693392*.html",
        ),
        (
            ("filters", ()),
            ("inherited_members", True),
            ("members", ("module_attribute",)),
        ): external("a31023e1ab99*.html"),
        (("filters", None), ("inherited_members", ()), ("members", None)): external(
            "decb32481637*.html",
        ),
        (
            ("filters", None),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("06d6f0fbe7d2*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", ()),
        ): external("0d64783aa6b3*.html"),
        (("filters", None), ("inherited_members", True), ("members", ())): external(
            "e705bc6a2bf4*.html",
        ),
        (
            ("filters", ()),
            ("inherited_members", False),
            ("members", ("module_attribute",)),
        ): external("9b9d730a9ab2*.html"),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ("method1",)),
            ("members", True),
        ): external("5666a554062c*.html"),
        (("filters", None), ("inherited_members", ()), ("members", False)): external(
            "52f22ff10a8a*.html",
        ),
        (("filters", ()), ("inherited_members", False), ("members", True)): external(
            "0896812735b0*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", True),
            ("members", False),
        ): external("a55aa2869dc3*.html"),
        (("filters", None), ("inherited_members", False), ("members", True)): external(
            "fd9bc4ba54f6*.html",
        ),
        (
            ("filters", ("!module_attribute",)),
            ("inherited_members", ()),
            ("members", ("module_attribute",)),
        ): external("7cce41ff77bf*.html"),
    },
)
