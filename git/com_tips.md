#### 删除某次commit
1. 找到要删除的提交的前一次
``` git rebase -i <commit-hash> ```
or 
``` git rebase -i HEAD~n```
2. 编辑提交信息，将`pick`改成`edit`或者`e`
3. git停在编辑的提交上，可以删除它
```git reset HEAD^```
4. 解决冲突或者取消操作
```git rebase --continue```
```git rebase --abort```

