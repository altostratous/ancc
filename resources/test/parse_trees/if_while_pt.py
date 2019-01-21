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


if_while_expected_parse_tree = ('program', [
    ('declaration-list', [
        ('type-specifier', ['int']),
        'ID',
        ('declaration', [
            ('var-declaration', [
                '[', 'NUM', ']', ';'
            ])
        ]),
        ('declaration-list', [
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
                            ('type-specifier', ['int']),
                            'ID',
                            ('declaration', [
                                ('var-declaration', [';']),
                            ]),
                            ('declaration-list', []),
                        ]),
                        ('statement-list', [
                            ('statement', [
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
                            ]),
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
                                                            ('reference', [
                                                                ('call', [
                                                                    '(',
                                                                    ('args', [
                                                                        ('arg-list', [
                                                                            id_expression,
                                                                            ('arg-list-prime', []),
                                                                        ])
                                                                    ]),
                                                                    ')'
                                                                ]),
                                                            ]),
                                                            ('term-prime', []),
                                                        ]),
                                                        ('additive-expression-prime', []),
                                                    ]),
                                                    ('rest-of-simple-expression', []),
                                                ])
                                            ])
                                        ]),
                                        ')',
                                        ('statement', [
                                            ('return-stmt', [
                                                'return',
                                                ('rest-of-return-stmt', [';'])
                                            ])
                                        ]),
                                        'else',
                                        ('statement', [
                                            ('iteration-stmt', [
                                                'while',
                                                '(',
                                                id_expression,
                                                ')',
                                                ('statement', [
                                                    ('compound-stmt', [
                                                        '{',
                                                        ('declaration-list', []),
                                                        ('statement-list', [
                                                            ('statement', [
                                                                ('expression-stmt', [
                                                                    ('expression', [
                                                                        'ID',
                                                                        ('id-expression', [
                                                                            '[',
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
                                                                            ']',
                                                                            ('bracket-id-expression', [
                                                                                '=',
                                                                                id_expression
                                                                            ]),
                                                                        ]),
                                                                    ]),
                                                                    ';',
                                                                ])
                                                            ]),
                                                            ('statement-list', [
                                                                ('statement', [
                                                                    ('expression-stmt', [
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
                                                                        ';',
                                                                    ]),
                                                                ]),
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
                                                                                                                        '[',
                                                                                                                        id_expression,
                                                                                                                        ']',
                                                                                                                        ('bracket-id-expression', []),
                                                                                                                    ]),
                                                                                                                ]),
                                                                                                                ('arg-list-prime',
                                                                                                                 []),
                                                                                                            ])
                                                                                                        ]),
                                                                                                        ')',
                                                                                                    ])
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
                                                                    ('statement-list', []),
                                                                ]),
                                                            ]),
                                                        ]),
                                                        '}',
                                                    ]),
                                                ]),
                                            ]),
                                        ]),
                                    ])
                                ]),
                                ('statement-list', []),
                            ]),
                        ]),
                        '}',
                    ]),
                ]),
            ]),
            ('declaration-list', []),
        ]),
    ]),
    'EOF',
])
