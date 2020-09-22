# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Considere um modelo de informação, onde um registro é representado por uma "tupla".
# Uma tupla (ou lista) nesse contexto é chamado de fato.

# Exemplo de um fato:
# ('joão', 'idade', 18, True)

# Nessa representação, a entidade (E) 'joão' tem o atributo (A) 'idade' com o valor (V) '18'.

# Para indicar a remoção (ou retração) de uma informação, o quarto elemento da tupla pode ser 'False'
# para representar que a entidade não tem mais aquele valor associado aquele atributo.


# Como é comum em um modelo de entidades, os atributos de uma entidade pode ter cardinalidade 1 ou N (muitos).

# Segue um exemplo de fatos no formato de tuplas (i.e. E, A, V, added?)

facts = [
  ('gabriel', 'endereço', 'av rio branco, 109', True),
  ('joão', 'endereço', 'rua alice, 10', True),
  ('joão', 'endereço', 'rua bob, 88', True),
  ('joão', 'telefone', '234-5678', True),
  ('joão', 'telefone', '91234-5555', True),
  ('joão', 'telefone', '234-5678', False),
  ('gabriel', 'telefone', '98888-1111', True),
  ('gabriel', 'telefone', '56789-1010', True),
]


# Vamos assumir que essa lista de fatos está ordenada dos mais antigos para os mais recentes.


# Nesse schema,
# o atributo 'telefone' tem cardinalidade 'muitos' (one-to-many), e 'endereço' é 'one-to-one'.
schema = [
    ('endereço', 'cardinality', 'one'),
    ('telefone', 'cardinality', 'many')
]


# Nesse exemplo, os seguintes registros representam o histórico de endereços que joão já teve:
#  (
#   ('joão', 'endereço', 'rua alice, 10', True)
#   ('joão', 'endereço', 'rua bob, 88', True),
#)
# E o fato considerado vigente (ou ativo) é o último.


# O objetivo desse desafio é escrever uma função que retorne quais são os fatos vigentes sobre essas entidades.
# Ou seja, quais são as informações que estão valendo no momento atual.
# A função deve receber `facts` (todos fatos conhecidos) e `schema` como argumentos.


# Resultado esperado para este exemplo (mas não precisa ser nessa ordem):
# [
#   ('gabriel', 'endereço', 'av rio branco, 109', True),
#   ('joão', 'endereço', 'rua bob, 88', True),
#   ('joão', 'telefone', '91234-5555', True),
#   ('gabriel', 'telefone', '98888-1111', True),
#   ('gabriel', 'telefone', '56789-1010', True)
# ]


def verify_vigency(facts, schema):
    schema_dict = {}
    for s in schema:
        schema_dict[s[0]] = s[2]

    facts_dict = {}

    for fact in facts:
        f_name = fact[0]
        f_param = fact[1]
        f_value = fact[2]
        f_added = fact[3]

        if f_added:
            if f_param in schema_dict and schema_dict[f_param] == 'many':

                if f_name not in facts_dict:
                    facts_dict[f_name] = {}
                else:
                    if (f_param in facts_dict[f_name]):
                        facts_dict[f_name][f_param].append(f_value)
                    else:
                        facts_dict[f_name][f_param] = [f_value]

            else:
                
                if f_name not in facts_dict:
                    facts_dict[f_name] = {}

                facts_dict[f_name][f_param] = f_value

        else:
            if f_param in schema_dict and schema_dict[f_param] == 'many':

                # Verifico se existe os dicionarios para name e param
                if (f_name in facts_dict) and (f_param in facts_dict[f_name]):

                    # Percorro a lista do parametro do caso de ser uma cardinalidade many
                    for value in range(0, len(facts_dict[f_name][f_param])):
                        if facts_dict[f_name][f_param][value] == f_value:
                            del facts_dict[f_name][f_param][value]
                            break

            else:
                if (f_name in facts_dict) and (f_param in facts_dict[f_name]):

                    # Verifico se o valor preenchido é o proprio para remoção
                    if facts_dict[f_name][f_param] == f_value:
                        del facts_dict[f_name][f_param]


    facts_list = []            
    for name, params in facts_dict.items():
        for k, values in params.items():
            if type(values) == list:
                for v in values:
                    fact = (name, k, v, True)
                    facts_list.append(fact)
            else:
                fact = (name, k, values, True)
                facts_list.append(fact)


    return facts_list


print(verify_vigency(facts, schema))