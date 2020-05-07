## Laboratory 1
### list of group members:
Name:Chen ZhengHui  id:192050190

Name:Li Xiang  id:192050189

###laboratory work number:
variant5
###variant description:
Hash-map (collision resolution: open addressing, for the array you can use built-in list) based set.

###synopsis:
mutable version used list to create a hashmap

immutable version used tuple to create a hashmap


###contribution summary for each group member:
mutable&mutable_test: Li Xiang

immutable&immutable_test Chen ZhengHui

###explanation of taken design decisions and analysis:
mutable version used list to create a hashmap because list can be changed and use Linear detection to solve the
collision,when collision happen,let the index+=1,and check if new index has collision,finally,find a index that don't have collision

immutable version used 10 elements tuple to create a hashmap because tuple can't be changed and use a Linear detection to solve the
collision,and f is Remainder method,,when collision happen,let the index+=1,and check if new index has collision,finally,find a index that don't have collision

###conclusion:
HashMap is a collection used to store key value. Each key value pair is also called an entry. These key value pairs are stored in an array, which is the backbone of HashMap.

HashMap is very fast

Linear exploration is the simplest method to deal with conflicts by using open addressing method. It starts from the D unit where conflicts occur and then explores the next unit in turn

Square exploration is a better way to deal with conflicts, which can avoid accumulation. Its disadvantage is that it cannot probe all cells on the hash table, but at least half of them can be detected