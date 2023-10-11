deflinearsearchproduct(productList,targetproduct):
 indices=[] 
 for index,product in enumerate(productList):
   if product==targetproduct:
    indices.append(index)
  return indices
product=["shoes","boot","loafer","shoes","sandals","shoes"]
target="shoes"
result=linearsearchproduct(product,target)
print(result)
