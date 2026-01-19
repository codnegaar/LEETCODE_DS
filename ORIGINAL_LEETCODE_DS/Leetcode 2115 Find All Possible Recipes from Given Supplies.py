'''
Leetcode 2115 Find All Possible Recipes from Given Supplies
 
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name
recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes,
i.e., ingredients[i] may contain a string that is in recipes.
You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
Return a list of all the recipes that you can create. You may return the answer in any order.
Note that two recipes may contain each other in their ingredients. 

Example 1:
        Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
        Output: ["bread"]
        Explanation:
        We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:
        Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
        Output: ["bread","sandwich"]
        Explanation:
        We can create "bread" since we have the ingredients "yeast" and "flour".
        We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Example 3:
        Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
        Output: ["bread","sandwich","burger"]
        Explanation:
        We can create "bread" since we have the ingredients "yeast" and "flour".
        We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
        We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
         

Constraints:
        n == recipes.length == ingredients.length
        1 <= n <= 100
        1 <= ingredients[i].length, supplies.length <= 100
        1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
        recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
        All the values of recipes and supplies combined are unique.
        Each ingredients[i] does not contain any duplicate values.

'''

from collections import defaultdict, deque
from typing import List

class Solution:
    """
    Solution class to determine which recipes can be prepared given initial supplies.
    """
    def findAllRecipes(
        self, 
        recipes: List[str], 
        ingredients: List[List[str]], 
        supplies: List[str]
    ) -> List[str]:
        """
        Determines the list of recipes that can be created based on available supplies.

        :param recipes: List of recipe names.
        :param ingredients: List of ingredient lists corresponding to each recipe.
        :param supplies: List of initial available supplies.
        :return: List of recipes that can be prepared.
        """
        # Convert supplies to a set for O(1) lookup
        available_supplies = set(supplies)

        # Map each recipe to its index
        recipe_to_index = {recipe: idx for idx, recipe in enumerate(recipes)}

        # Dependency graph tracking ingredients to dependent recipes
        dependency_graph = defaultdict(list)

        # In-degree array to track dependencies for each recipe
        in_degree = [0] * len(recipes)

        # Build dependency graph and count in-degrees
        for recipe_idx, ingredient_list in enumerate(ingredients):
            for ingredient in ingredient_list:
                if ingredient not in available_supplies:
                    dependency_graph[ingredient].append(recipes[recipe_idx])
                    in_degree[recipe_idx] += 1  # Increase in-degree since it depends on an unavailable ingredient

        # Initialize queue with recipes that have all ingredients available
        queue = deque(idx for idx, count in enumerate(in_degree) if count == 0)
        created_recipes = []

        # Process the queue using Topological Sorting (KahnΓÇÖs Algorithm)
        while queue:
            recipe_idx = queue.popleft()
            recipe = recipes[recipe_idx]
            created_recipes.append(recipe)

            # Reduce in-degree of dependent recipes and enqueue if they become available
            for dependent_recipe in dependency_graph[recipe]:
                dependent_idx = recipe_to_index[dependent_recipe]
                in_degree[dependent_idx] -= 1
                if in_degree[dependent_idx] == 0:
                    queue.append(dependent_idx)

        return created_recipes
