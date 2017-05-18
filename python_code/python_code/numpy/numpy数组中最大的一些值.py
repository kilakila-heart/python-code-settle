#--*coding:utf-8 --*
import numpy as np
output_prob=np.arange(12).reshape(4,3)
print output_prob.argmax()
print output_prob.argmin()
print output_prob
output_prob_after_flat=output_prob.flatten()
tmp_acc_index=output_prob_after_flat.argsort() #返回数组从小到大排序后的索引
tmp_dec_index=output_prob_after_flat.argsort()[::-1] #反转索引,相当于从大到小索引
#取出最大的五个数
top_inds = output_prob_after_flat.argsort()[::-1][:5]  # reverse sort and take five largest items
print output_prob_after_flat[top_inds]

