test2_expected_parse_tree = ('program', [
    ('declaration-list', [
        ('declaration-list-prime', [
            ('type-specifier', ['int']),
            'ID',
            ('declaration', [
                ('var-declaration', [
                    ('rest-of-var-declaration', [';'])
                ])
            ]),
            ('declaration-list-prime', [
                ('type-specifier', ['void']),
                'ID',
                ('declaration', [
                    ('var-declaration', [
                        ('rest-of-var-declaration', ['[', 'NUM', ']', ';'])
                    ])
                ]),
                ('declaration-list-prime', [
                    ('type-specifier', ['int']),
                    'ID',
                    ('declaration', [
                        ('fun-declaration', [
                            '(',
                            ('params', [
                                ('void-starting-param-list', [
                                    'void',
                                    ('rest-of-void-starting-param-list', []),
                                    ])
                                ])
                            ]),
                            ')',
                            ('compound_stmt', [
                                '{',
                                ('declaration-list', [
                                    ('declaration-list-prime', [])
                                ]),
                                ('statement-list', [
                                    ('statement-list-prime', [])
                                ]),
                                '}',
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ])
