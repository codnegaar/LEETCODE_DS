/***
  "Bottom-up" Solution
"Bottom-up" is another recursive solution. In each recursive call, we will firstly call the function recursively for all the children nodes and then 
come up with the answer according to the returned values and the value of the current node itself. This process can be regarded as a kind of postorder
traversal. Typically, a "bottom-up" recursive function bottom_up(root) will be something like this:
1. return specific value for null node
2. left_ans = bottom_up(root.left)      // call function recursively for left child
3. right_ans = bottom_up(root.right)    // call function recursively for right child
4. return answers                       // answer <-- left_ans, right_ans, root.val
Let's go on discussing the question about maximum depth but using a different way of thinking: for a single node of the tree, what will be the 
maximum depth x of the subtree rooted at itself?

If we know the maximum depth l of the subtree rooted at its left child and the maximum depth r of the subtree rooted at its right child, can we
answer the previous question? Of course yes, we can choose the maximum between them and add 1 to get the maximum depth of the subtree rooted at
the current node. That is x = max(l, r) + 1.

It means that for each node, we can get the answer after solving the problem for its children. Therefore, we can solve this problem using a 
"bottom-up" solution. Here is the pseudocode for the recursive function maximum_depth(root):

1. return 0 if root is null                 // return 0 for null node
2. left_depth = maximum_depth(root.left)
3. right_depth = maximum_depth(root.right)
4. return max(left_depth, right_depth) + 1  // return depth of the subtree rooted at root
 ***/

public int maximum_depth(TreeNode root) {
    if (root == null) {
        return 0;                                   // return 0 for null node
    }
    int left_depth = maximum_depth(root.left);
    int right_depth = maximum_depth(root.right);
    return Math.max(left_depth, right_depth) + 1;   // return depth of the subtree rooted at root
}


