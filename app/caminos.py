caminos= {
    "abrir_hustle":{
        "config": {
            "tiempo":10
        },
        "pasos":[
            {"img":"bluestacks.PNG","accion":"doble"}
        ]
    },
    "jugar_arena":{
        "config": {
            "tiempo_ejecucion":120,
            "ciclos": 18,
            "tiempo_pasos":2
        },
        "pasos":[  
            {"img":"mapa.PNG","accion":"click"},
            {"img":"arena.PNG","accion":"click"},
            {"img":"participar_arena_boletos.PNG","accion":"click"},
            {"img":"participar.PNG","accion":"click"},
            {"img":"arena_confirmar.PNG","accion":"click"},
            {"img": "general_castillo.PNG" ,"accion":"ARENA"},
            {"img":"arena_reclamar.PNG","accion":"click","final":1},
        ]
    },
    "jugar_arena_adentro":{
        "config":{
            "tiempo_ejecucion":10,
            "tiempo_pasos":4
        },   
    
        "pasos": [
            {"img":"arena_elegir_oponente.PNG","accion":"elegir_oponente"}, 
            {"img": "arena_atacar.PNG","accion":"click","accion_no_encuentra":"add_no_atacar"},
            {"img": "arena_cerrar_ataque.PNG","accion":["arena_no_atacar","click"]},
            # {"img": "arena_cerrar_ataque.PNG","accion":"click"},
            {"img": "arena_atacando.PNG","accion":"esperar","esperar":15},
            {"img": "arena_victoria.PNG","accion":"arena_resultados","resultado":"victoria"},
            {"img": "arena_derrota.PNG","accion":"arena_resultados","resultado":"derrota"},
            
            {"img": "arena_castillo.PNG" ,"accion":["final_batalla","click"]}, 
            # {"img": "arena_castillo.PNG" ,"accion":"final_batalla"}, 
            # {"img": "arena_castillo.PNG" ,"accion":"click"},            
            {"img":"arena_reclamar.PNG","accion":"final_arena","final":1},
        ],
    },
    "portal": {
        "config": {
            "tiempo":3
        },
        "pasos":[
            {"img":"portal_nivel80.PNG","accion":"click"},
            {"img":"portal_atacar55k.PNG","accion":"click"},
            {"img":"portal_castillo.PNG","accion":"click"},
            {"img":"portal_si_pelear.PNG","accion":"click"}


        ]
    }



}