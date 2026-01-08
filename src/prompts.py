"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                           YOUR TASK PROMPTS                                   ║
║                                                                               ║
║  CUSTOMIZE THIS FILE to define prompts/instructions for your task.            ║
║  Prompts are selected based on task type and returned to the model.           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import random


# ══════════════════════════════════════════════════════════════════════════════
#  DEFINE YOUR PROMPTS
# ══════════════════════════════════════════════════════════════════════════════

PROMPTS = {
    "default": [
        "Given the refractive index of glass = {n_glass:.2f}, predict the refraction of light through the glass. The refracted ray should extend to the edge of the image.",
        "Given the glass refractive index = {n_glass:.2f}, predict how light refracts when passing through the glass. Extend the refracted ray to the image edge.",
        "Given the refractive index of glass = {n_glass:.2f}, predict the light refraction through the glass surface. The refracted ray must extend all the way to the edge of the image.",
    ],
}


def get_prompt(task_type: str = "default", task_data: dict = None) -> str:
    """
    Select a random prompt for the given task type.
    
    Args:
        task_type: Type of task (key in PROMPTS dict)
        task_data: Task data dictionary containing n_glass
        
    Returns:
        Random prompt string from the specified type with refractive index filled in
    """
    prompts = PROMPTS.get(task_type, PROMPTS["default"])
    prompt_template = random.choice(prompts)
    
    # Fill in the refractive index if task_data is provided
    if task_data and "n_glass" in task_data:
        return prompt_template.format(n_glass=task_data["n_glass"])
    else:
        # Fallback if no task_data provided
        return prompt_template.format(n_glass=1.5)


def get_all_prompts(task_type: str = "default") -> list[str]:
    """Get all prompts for a given task type."""
    return PROMPTS.get(task_type, PROMPTS["default"])


# ══════════════════════════════════════════════════════════════════════════════
#  NOTE: This generator does not use rubrics
# ══════════════════════════════════════════════════════════════════════════════
#
# The TaskPair schema only includes:
#   - task_id, domain, prompt
#   - first_image, final_image  
#   - ground_truth_video (optional)
#
# No rubric field exists in the schema, so only prompts are generated.
# ══════════════════════════════════════════════════════════════════════════════
