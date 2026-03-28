#!/usr/bin/env python3
"""
任务分析脚本
分析用户任务描述，识别类型、复杂度、约束条件
"""

import json
import sys
import re

# 关键词匹配规则
TASK_PATTERNS = {
    'mvp-development': {
        keywords: ['MVP', '快速验证', '最小可行', '试水', '创业'],
        complexity: 'simple',
        duration_weeks: [2, 4]
    },
    'full-stack-app': {
        keywords: ['完整应用', '商业级', '正式发布', '产品上线'],
        complexity: 'complex',
        duration_weeks: [8, 12]
    },
    'enterprise-system': {
        keywords: ['企业级', '大型系统', '高并发', '分布式', '多模块'],
        complexity: 'very_complex',
        duration_weeks: [12, 24]
    }
}

COMPLEXITY_INDICATORS = {
    'simple': ['简单', '基础', '单个功能', '小'],
    'medium': ['中等', '多个功能', '标准'],
    'complex': ['复杂', '完整', '系统', '多模块'],
    'very_complex': ['非常复杂', '大型', '企业级', '平台']
}

CONSTRAINT_PATTERNS = {
    'budget': r'预算\s*[:：]?\s*(\d+(?:\.\d+)?[万]?)',
    'deadline': r'(工期 | 时间|周期|多久)\s*[:：]?\s*(\d+(?:\.\d+)?[个周天月]?)',
    'urgent': r'紧急 | 着急 | 尽快 | 马上 | 快点'
}

def analyze_complexity(text):
    """分析任务复杂度"""
    score = 0
    
    for complexity, indicators in COMPLEXITY_INDICATORS.items():
        for indicator in indicators:
            if indicator in text:
                if complexity == 'simple':
                    score -= 1
                elif complexity == 'medium':
                    score += 0
                elif complexity == 'complex':
                    score += 1
                elif complexity == 'very_complex':
                    score += 2
    
    # 基于文本长度简单估算
    if len(text) > 200:
        score += 1
    if len(text) > 500:
        score += 1
    
    # 映射到复杂度等级
    if score <= 0:
        return 'simple'
    elif score <= 1:
        return 'medium'
    elif score <= 2:
        return 'complex'
    else:
        return 'very_complex'

def extract_constraints(text):
    """提取约束条件"""
    constraints = {}
    
    # 预算
    budget_match = re.search(CONSTRAINT_PATTERNS['budget'], text)
    if budget_match:
        budget_str = budget_match.group(1)
        if '万' in budget_str:
            constraints['budget'] = float(budget_str.replace('万', '')) * 10000
        else:
            constraints['budget'] = float(budget_str)
    
    # 工期
    deadline_match = re.search(CONSTRAINT_PATTERNS['deadline'], text)
    if deadline_match:
        time_value = deadline_match.group(2)
        constraints['deadline'] = time_value
    
    # 紧急程度
    if re.search(CONSTRAINT_PATTERNS['urgent'], text):
        constraints['urgent'] = True
    
    return constraints

def match_scenario(text):
    """匹配场景"""
    for scenario_id, config in TASK_PATTERNS.items():
        for keyword in config['keywords']:
            if keyword in text:
                return scenario_id, config['complexity']
    
    # 默认返回基于复杂度的场景
    complexity = analyze_complexity(text)
    if complexity == 'simple':
        return 'mvp-development', 'simple'
    elif complexity == 'medium':
        return 'mvp-development', 'medium'
    elif complexity == 'complex':
        return 'full-stack-app', 'complex'
    else:
        return 'enterprise-system', 'very_complex'

def main():
    if len(sys.argv) < 2:
        print("Usage: analyze_task.py \"task description\"")
        sys.exit(1)
    
    task_description = ' '.join(sys.argv[1:])
    
    # 分析任务
    scenario_id, default_complexity = match_scenario(task_description)
    complexity = analyze_complexity(task_description)
    constraints = extract_constraints(task_description)
    
    # 使用更准确的复杂度
    final_complexity = complexity if complexity != 'simple' else default_complexity
    
    result = {
        'scenarioId': scenario_id,
        'complexity': final_complexity,
        'constraints': constraints,
        'originalText': task_description
    }
    
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
