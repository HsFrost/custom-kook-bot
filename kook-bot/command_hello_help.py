def help(str=''):
    print(str)
    return """    
**命令**
你好
`.hello {指令}`
`指令:`
        `空值（不填任何参数）:`打招呼
        `help:`显示帮助文档
        `time:`显示当前时间

APEX LEGENDS信息查询
`.apex {指令,参数1,参数2}`
`指令:`
        `地图:`
                暂未实装
        `查询:`
                `参数1:`玩家ID
                `参数2:`玩家平台（可不填，默认Origin，不支持steamID） {'PC'(Origin or Steam),'PS4'(Playstation 4/5) or 'X1'(Xbox)}

掷色子
`.roll {最小值，最大值，掷几次}`    
"""
