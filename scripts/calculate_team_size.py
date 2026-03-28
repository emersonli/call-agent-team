#!/usr/bin/env python3
"""
团队规模计算脚本
根据任务复杂度和约束条件计算各角色数量
"""

import yaml
import json
import sys
from pathlib import Path

def load_config(config_path):
    """加载团队配置文件"""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def calculate_role_count(role, complexity, constraints, scenario=None):
    """计算单个角色的数量"""
    base_count = role.get('defaultCount', 1)
    max_count = role.get('maxCount', 5)
    
    # 复杂度调整系数
    complexity_multipliers = {
        'simple': 0.5,
        'medium': 1.0,
        'complex': 1.5,
        'very_complex': 2.0
    }
    multiplier = complexity_multipliers.get(complexity, 1.0)
    
    # 场景特定配置优先
    if scenario and 'roles' in scenario:
        for scenario_role in scenario['roles']:
            if scenario_role.get('roleId') == role.get('roleId'):
                return scenario_role.get('count', int(base_count * multiplier))
    
    # 预算约束调整
    budget = constraints.get('budget', float('inf'))
    base_hourly_rate = role.get('baseHourlyRate', 1000)
    estimated_hours = 40  # 基准工时
    
    if budget < (base_hourly_rate * estimated_hours * 0.7):
        # 预算不足，减少人手
        adjusted_count = max(0, int(base_count * 0.7))
    elif budget > (base_hourly_rate * estimated_hours * 3):
        # 预算充足，增加人手
        adjusted_count = min(max_count, int(base_count * multiplier * 1.2))
    else:
        # 标准配置
        adjusted_count = min(max_count, max(1, int(base_count * multiplier)))
    
    # 时间紧急程度调整
    if constraints.get('urgent', False):
        adjusted_count = min(max_count, int(adjusted_count * 1.5))
    
    return adjusted_count

def main():
    if len(sys.argv) < 3:
        print("Usage: calculate_team_size.py <config.yaml> <complexity> [scenario]")
        print("Complexity: simple/medium/complex/very_complex")
        sys.exit(1)
    
    config_path = sys.argv[1]
    complexity = sys.argv[2]
    scenario_id = sys.argv[3] if len(sys.argv) > 3 else None
    
    # 从环境变量或参数获取约束条件
    constraints = {}
    if len(sys.argv) > 4:
        constraints = json.loads(sys.argv[4])
    
    # 加载配置
    config = load_config(config_path)
    
    # 查找场景配置
    scenario = None
    if scenario_id and 'scenarios' in config:
        for s in config['scenarios']:
            if s.get('scenarioId') == scenario_id:
                scenario = s
                break
    
    # 计算团队配置
    team_config = {
        'teamType': config.get('teamType'),
        'scenario': scenario_id,
        'complexity': complexity,
        'constraints': constraints,
        'roles': []
    }
    
    total_cost = 0
    for role in config.get('rolePool', []):
        count = calculate_role_count(role, complexity, constraints, scenario)
        if count > 0:
            hourly_rate = role.get('baseHourlyRate', 1000)
            estimated_hours = 40 * count  # 简化估算
            
            role_config = {
                'roleId': role.get('roleId'),
                'title': role.get('title'),
                'count': count,
                'hourlyRate': hourly_rate,
                'estimatedHours': estimated_hours,
                'estimatedCost': hourly_rate * estimated_hours
            }
            
            team_config['roles'].append(role_config)
            total_cost += role_config['estimatedCost']
    
    team_config['totalEstimatedCost'] = total_cost
    team_config['currency'] = config.get('constraints', {}).get('budget', {}).get('currency', 'CNY')
    
    # 输出 JSON
    print(json.dumps(team_config, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
