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

switch_expected_parse_tree = ('program', [
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
                        ('void-starting-param-list', [
                            'void',
                            ('rest-of-void-starting-param-list', []),
                        ])
                    ]),
                    ')',
                    ('compound-stmt', [
                        '{',
                        ('declaration-list', [
                            ('type-specifier', ['int']),
                            'ID',
                            ('declaration', [
                                ('var-declaration', [';']),
                            ]),
                            ('declaration-list', []),
                        ]),
                        ('statement-list', [
                            id_equals_num_stmt,
                            ('statement-list', [
                                ('statement', [
                                    ('switch-stmt', [
                                        'switch',
                                        '(',
                                        id_expression,
                                        ')',
                                        '{',
                                        ('case-stmts', [
                                            ('case-stmt', [
                                                'case',
                                                'NUM',
                                                ':',
                                                ('statement-list', [
                                                    ('statement', [
                                                        ('expression-stmt', [
                                                            ('expression', [
                                                                'ID',
                                                                ('id-expression', [
                                                                    '=',
                                                                    id_expression
                                                                ])
                                                            ]),
                                                            ';'
                                                        ])
                                                    ]),
                                                    ('statement-list', [
                                                        ('statement', [
                                                            ('expression-stmt', [
                                                                'break',
                                                                ';'
                                                            ])
                                                        ]),
                                                        ('statement-list', [])
                                                    ])
                                                ])
                                            ]),
                                            ('case-stmts', [
                                                ('case-stmt', [
                                                    'case',
                                                    'NUM',
                                                    ':',
                                                    ('statement-list', [
                                                        ('statement', [
                                                            ('expression-stmt', [
                                                                ('expression', [
                                                                    'ID',
                                                                    ('id-expression', [
                                                                        '=',
                                                                        ('expression', [
                                                                            'ID',
                                                                            ('id-expression', [
                                                                                ('id-simple-expression', [
                                                                                    ('id-additive-expression', [
                                                                                        ('id-term', [
                                                                                            ('reference', []),
                                                                                            ('term-prime', [])
                                                                                        ]),
                                                                                        ('additive-expression-prime', [
                                                                                            ('addop', ['-']),
                                                                                            ('term', [
                                                                                                ('factor', ['NUM']),
                                                                                                ('term-prime', []),
                                                                                            ]),
                                                                                            ('additive-expression-prime', []),
                                                                                        ])
                                                                                    ]),
                                                                                    ('rest-of-simple-expression', []),
                                                                                ])
                                                                            ])
                                                                        ])
                                                                    ])
                                                                ]),
                                                                ';'
                                                            ])
                                                        ]),
                                                        ('statement-list', [
                                                            ('statement', [
                                                                ('expression-stmt', [
                                                                    'break',
                                                                    ';'
                                                                ])
                                                            ]),
                                                            ('statement-list', [])
                                                        ])
                                                    ])
                                                ]),
                                                ('case-stmts', [
                                                    ('case-stmt', [
                                                        'case',
                                                        'NUM',
                                                        ':',
                                                        ('statement-list', [
                                                            ('statement', [
                                                                ('expression-stmt', [
                                                                    ('expression', [
                                                                        'ID',
                                                                        ('id-expression', [
                                                                            '=',
                                                                            ('expression', [
                                                                                'ID',
                                                                                ('id-expression', [
                                                                                    ('id-simple-expression', [
                                                                                        ('id-additive-expression', [
                                                                                            ('id-term', [
                                                                                                ('reference', []),
                                                                                                ('term-prime', [])
                                                                                            ]),
                                                                                            ('additive-expression-prime', [
                                                                                                ('addop', ['+']),
                                                                                                ('term', [
                                                                                                    ('factor', ['NUM']),
                                                                                                    ('term-prime', []),
                                                                                                ]),
                                                                                                ('additive-expression-prime', []),
                                                                                            ])
                                                                                        ]),
                                                                                        ('rest-of-simple-expression', []),
                                                                                    ])
                                                                                ])
                                                                            ])
                                                                        ])
                                                                    ]),
                                                                    ';'
                                                                ])
                                                            ]),
                                                            ('statement-list', [
                                                                ('statement', [
                                                                    ('expression-stmt', [
                                                                        'break',
                                                                        ';'
                                                                    ])
                                                                ]),
                                                                ('statement-list', [])
                                                            ])
                                                        ])
                                                    ]),
                                                    ('case-stmts', []),
                                                ]),
                                            ])
                                        ]),
                                        ('default-stmt', [
                                            'default',
                                            ':',
                                            ('statement-list', [
                                                id_equals_num_stmt,
                                                ('statement-list', [])
                                            ]),
                                        ]),
                                        '}',
                                    ])
                                ]),
                                ('statement-list', [
                                    ('statement', [
                                        ('return-stmt', [
                                            'return',
                                            ('rest-of-return-stmt', [
                                                id_expression,
                                                ';'
                                            ])
                                        ])
                                    ]),
                                    ('statement-list', [])
                                ]),
                            ])
                        ]),
                    '}',
                    ]),
                ]),
            ]),
            ('declaration-list', []),
        ]),
    ]),
    'EOF'
])