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

id_equals_num_stmt = ('statement', [
                        ('expression-stmt', [
                            ('expression', [
                                'ID',
                                ('id-expression', [
                                    '=',
                                    ('expression', [
                                        ('simple-expression', [
                                            ('additive-expression', [
                                                ('term', [
                                                    ('factor', ['NUM']),
                                                    ('term-prime', []),
                                                ]),
                                                ('additive-expression-prime', []),
                                            ]),
                                            ('rest-of-simple-expression', []),
                                        ])
                                    ]),
                                ]),
                            ]),
                            ';',
                        ]),
                    ])

easy_expected_parse_tree = ('program', [
    ('declaration-list', [
        ('type-specifier', ['int']),
        'ID',
        ('declaration', [
            ('var-declaration', [';'])
        ]),
        ('declaration-list', [
            ('type-specifier', ['int']),
            'ID',
            ('declaration', [
                ('fun-declaration', [
                    '(',
                    ('params', [
                        ('int-starting-param-list', [
                            'int',
                            'ID',
                            ('rest-of-param', []),
                            ('param-list-prime', []),
                        ])
                    ]),
                    ')',
                    ('compound-stmt', [
                        '{',
                        ('declaration-list', []),
                        ('statement-list', [
                            id_equals_num_stmt,
                            ('statement-list', [
                                id_equals_num_stmt,
                                ('statement-list', [
                                    ('statement', [
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
                                                                                ('expression', [
                                                                                    'ID',
                                                                                    ('id-expression', [
                                                                                        ('id-simple-expression', [
                                                                                            ('id-additive-expression', [
                                                                                                ('id-term', [
                                                                                                    ('reference', [
                                                                                                        ('call', [
                                                                                                            '(',
                                                                                                            ('args', []),
                                                                                                            ')',
                                                                                                        ]),
                                                                                                    ]),
                                                                                                    ('term-prime', [])
                                                                                                ]),
                                                                                                ('additive-expression-prime', [])
                                                                                            ]),
                                                                                            ('rest-of-simple-expression', [])
                                                                                        ])
                                                                                    ])
                                                                                ]),
                                                                                ('arg-list-prime', [
                                                                                    ',',
                                                                                    id_expression,
                                                                                    ('arg-list-prime', [])
                                                                                ])
                                                                            ])
                                                                        ]),
                                                                        ')'
                                                                    ])
                                                                ]),
                                                                ('term-prime', []),
                                                            ]),
                                                            ('additive-expression-prime', [])
                                                        ]),
                                                        ('rest-of-simple-expression', [])
                                                    ])
                                                ])
                                            ]),
                                            ';'
                                        ]),
                                    ]),
                                    ('statement-list', [
                                        ('statement', [
                                            ('return-stmt', [
                                                'return',
                                                ('rest-of-return-stmt', [
                                                    ('expression', [
                                                        ('simple-expression', [
                                                            ('additive-expression', [
                                                                ('term', [
                                                                    ('factor', ['NUM']),
                                                                    ('term-prime', []),
                                                                ]),
                                                                ('additive-expression-prime', []),
                                                            ]),
                                                            ('rest-of-simple-expression', []),
                                                        ])
                                                    ]),
                                                    ';'
                                                ])
                                            ])
                                        ]),
                                        ('statement-list', [])
                                    ]),
                                ])
                            ])
                        ]),
                        '}'
                    ]),
                ])
            ]),
            ('declaration-list', [])
        ])
    ]),
    'EOF',
])
