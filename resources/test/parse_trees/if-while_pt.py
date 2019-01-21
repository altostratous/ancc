if_while_expected_parse_tree = ('program', [
    ('declaration-list', [
        ('declaration-list-prime', [
            ('type-specifier', ['void']),
            'ID',
            ('declaration', [
                ('fun-declaration', [
                    '(',
                    ('params', [
                        ('void-starting-param-list', [
                            'void',
                            ('rest-of-void-starting-param-list', []),
                        ])
                    ]),
                    ')',
                    ('compound-stmt', [
                        '{',
                        ('declaration-list', [
                            ('declaration-list-prime', [])
                        ]),
                        ('statement-list', [
                            ('statement-list-prime', [
                                ('statement', [
                                    ('expression-stmt', [
                                        ('expression', [
                                            'ID',
                                            ('id-expression', [
                                                ('id-simple-expression', [
                                                    ('id-additive-expression', [
                                                        ('id-term', [
                                                            ('id-factor', [
                                                                ('reference', [
                                                                    ('call', [
                                                                        '(',
                                                                        ('args', [
                                                                            ('arg-list', [
                                                                                ('expression', [
                                                                                    (
                                                                                    'simple-expression',
                                                                                    [
                                                                                        (
                                                                                        'additive-expression',
                                                                                        [
                                                                                            ('term',
                                                                                             [
                                                                                                 (
                                                                                                 'factor',
                                                                                                 [
                                                                                                     'NUM'
                                                                                                 ]),
                                                                                                 (
                                                                                                 'term-prime',
                                                                                                 []),
                                                                                             ]),
                                                                                            (
                                                                                            'additive-expression-prime',
                                                                                            []),
                                                                                        ]),
                                                                                        (
                                                                                        'rest-of-simple-expression',
                                                                                        []),
                                                                                    ])
                                                                                ]),
                                                                                ('arg-list-prime',
                                                                                 []),
                                                                            ])
                                                                        ]),
                                                                        ')',
                                                                    ])
                                                                ]),
                                                            ]),
                                                            ('term-prime', []),
                                                        ]),
                                                        ('additive-expression-prime', []),
                                                    ]),
                                                    ('rest-of-simple-expression', []),
                                                ]),
                                            ])
                                        ]),
                                        ';'
                                    ])
                                ]),
                                ('statement-list-prime', []),
                            ])
                        ]),
                        '}',
                    ]),
                ]),
            ]),
            ('declaration-list-prime', []),
        ]),
    ]),
    'EOF',
])
