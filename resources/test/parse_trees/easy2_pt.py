id_expression = ('expression', [
                   'ID',
                    ('id-expression', [
                        ('id-simple-expression', [
                            ('id-additive-expression', [
                                ('id-term', [
                                    ('reference', []),
                                    ('term-prime', []),
                                ]),
                                ('additive-expression-prime', []),
                            ]),
                            ('rest-of-simple-expression', []),
                        ])
                    ]),
                ])

output_id_call_statement = ('statement', [
    ('expression-stmt', [
        ('expression', [
            'ID',
            ('id-expression', [
                ('id-simple-expression', [
                    ('id-additive-expression', [
                        ('id-term', [
                            ('reference', [
                                ('call', [
                                    '(',
                                    ('args', [
                                        ('arg-list', [
                                            id_expression,
                                            ('arg-list-prime', [])
                                        ])
                                    ]),
                                    ')'
                                ])
                            ]),
                            ('term-prime', [])
                        ]),
                        ('additive-expression-prime', []),
                    ]),
                    ('rest-of-simple-expression', []),
                ])
            ])
        ]),
        ';'
    ])
])

easy2_expected_parse_tree = ('program', [
    ('declaration-list', [
        ('type-specifier', ['void']),
        'ID',
        ('declaration', [
            ('fun-declaration', [
                '(',
                ('params', [
                    ('int-starting-param-list', [
                        'int',
                        'ID',
                        ('rest-of-param', []),
                        ('param-list-prime', [
                            ',',
                            ('param', [
                                ('type-specifier', ['int']),
                                'ID',
                                ('rest-of-param', [])
                            ]),
                            ('param-list-prime', [])
                        ]),
                    ])
                ]),
                ')',
                ('compound-stmt', [
                    '{',
                    ('declaration-list', []),
                    ('statement-list', [
                        ('statement', [
                            ('selection-stmt', [
                                'if',
                                '(',
                                ('expression', [
                                    'ID',
                                    ('id-expression', [
                                        ('id-simple-expression', [
                                            ('id-additive-expression', [
                                                ('id-term', [
                                                    ('reference', []),
                                                    ('term-prime', [])
                                                ]),
                                                ('additive-expression-prime', []),
                                            ]),
                                            ('rest-of-simple-expression', [
                                                'RELOP',
                                                ('addop-relop-rest', [
                                                    ('additive-expression', [
                                                        ('term', [
                                                            ('factor', ['NUM']),
                                                            ('term-prime', []),
                                                        ]),
                                                        ('additive-expression-prime', [])
                                                    ])
                                                ])
                                            ]),
                                        ])
                                    ])
                                ]),
                                ')',
                                output_id_call_statement,
                                'else',
                                output_id_call_statement,
                            ])
                        ]),
                        ('statement-list', [])
                    ]),
                    '}'
                ]),
            ])
        ]),
        ('declaration-list', [])
    ]),
    'EOF',
])
