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


final_expected_parse_tree = ('program', [
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
                                                                        'ID',
                                                                        ('id-additive-expression', [
                                                                            ('id-term', [
                                                                                ('reference', []),
                                                                                ('term-prime', []),
                                                                            ]),
                                                                            ('additive-expression-prime', []),
                                                                        ]),
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
                                                                                            ('expression', [
                                                                                                ('simple-expression', [
                                                                                                    ('additive-expression', [
                                                                                                        ('term', [
                                                                                                            ('factor', ['NUM']),
                                                                                                            ('term-prime', [
                                                                                                                '*',
                                                                                                                ('mult-rest', [
                                                                                                                    'ID',
                                                                                                                    ('id-term', [
                                                                                                                        ('reference', []),
                                                                                                                        ('term-prime', [
                                                                                                                            '*',
                                                                                                                            ('mult-rest', [
                                                                                                                                'ID',
                                                                                                                                ('id-term', [
                                                                                                                                    ('reference', []),
                                                                                                                                    ('term-prime', [

                                                                                                                                    ])
                                                                                                                                ])
                                                                                                                            ])
                                                                                                                        ])
                                                                                                                    ])
                                                                                                                ])
                                                                                                            ])
                                                                                                        ]),
                                                                                                        ('additive-expression-prime', [])
                                                                                                    ]),
                                                                                                    ('rest-of-simple-expression', [])
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
                                                                                                                    ('addop', ['-']),
                                                                                                                    ('addop-relop-rest', [
                                                                                                                        ('additive-expression', [
                                                                                                                            ('term', [
                                                                                                                                ('factor', ['NUM']),
                                                                                                                                ('term-prime', []),
                                                                                                                            ]),
                                                                                                                            ('additive-expression-prime', []),
                                                                                                                        ]),
                                                                                                                    ]),
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
                                                                                                                        ('addop-relop-rest', [
                                                                                                                            ('additive-expression', [
                                                                                                                                ('term', [
                                                                                                                                    ('factor', ['NUM']),
                                                                                                                                    ('term-prime', []),
                                                                                                                                ]),
                                                                                                                                ('additive-expression-prime', []),
                                                                                                                            ]),
                                                                                                                        ])
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
                        ]),
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
                    ])
                ]),
            ]),
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
                                                            ('rest-of-simple-expression', [
                                                                'RELOP',
                                                                ('addop-relop-rest', [
                                                                    'ID',
                                                                    ('id-additive-expression', [
                                                                        ('id-term', [
                                                                            ('reference', []),
                                                                            ('term-prime', []),
                                                                        ]),
                                                                        ('additive-expression-prime', [
                                                                            ('addop', ['+']),
                                                                            ('addop-relop-rest', [
                                                                                ('additive-expression', [
                                                                                    ('term', [
                                                                                        ('factor', ['NUM']),
                                                                                        ('term-prime', []),
                                                                                    ]),
                                                                                    ('additive-expression-prime', [
                                                                                        ('addop', ['-']),
                                                                                        ('addop-relop-rest', [
                                                                                            'ID',
                                                                                            ('id-additive-expression', [
                                                                                                ('id-term', [
                                                                                                    ('reference', []),
                                                                                                    ('term-prime', []),
                                                                                                ]),
                                                                                                ('additive-expression-prime', [])
                                                                                            ])
                                                                                        ])
                                                                                    ])
                                                                                ])
                                                                            ])
                                                                        ])
                                                                    ])
                                                                ])
                                                            ]),
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
                                                                                                                ('addop-relop-rest', [
                                                                                                                    ('additive-expression', [
                                                                                                                        ('term', [
                                                                                                                            ('factor', ['NUM']),
                                                                                                                            ('term-prime', []),
                                                                                                                        ]),
                                                                                                                        ('additive-expression-prime', []),
                                                                                                                    ]),
                                                                                                                ])
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
        ])
    ]),
    'EOF',
])
