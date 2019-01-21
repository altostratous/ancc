if_while_expected_parse_tree = ('program', [
    ('declaration-list', [
        ('type-specifier', ['int']),
        'ID',
        ('declaration', [
            ('var-declaration', [
                ('rest-of-var-declaration', ['[', 'NUM', ']'])
            ])
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
                                ('var-declaration', [
                                    ('rest-of-var-declaration', [';']),
                                ]),
                            ]),
                            ('declaration-list-', []),
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
                                                                            ('expression', [
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
                                                                            ]),
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
                                        ('expression', [
                                            ('return-stmt', [
                                                'return',
                                                ('rest-of-return-stmt', [';'])
                                            ])
                                        ]),
                                        'else',
                                        ('expression', [
                                            'while',
                                            '(',
                                            ('expression', [
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
                                            ]),
                                            ')',
                                            ('statement', [
                                                ('compound-stmt', [
                                                    '{',
                                                    ('declaration-list', []),
                                                    ('statement-list', [
                                                        ('statement', [

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
                                                                    ]),                                                                    ';',
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
                                                                                            ('id-factor', [
                                                                                                ('reference', [
                                                                                                    ('call', [
                                                                                                        '(',
                                                                                                        ('args', [
                                                                                                            ('arg-list', [
                                                                                                                ('expression', [
                                                                                                                    'ID',
                                                                                                                    ('id-expression', [
                                                                                                                        '[',
                                                                                                                        ('expression', [
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
                                                                                                                        ]),
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
