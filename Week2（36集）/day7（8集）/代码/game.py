# 游戏： 
'''

   1. 选择人物
   2. 购买武器  金币
   3. 打仗  赢 得金币
   4. 选择删除武器
   5. 查看武器
   6. 退出游戏

'''
import random


print('*'*40)
print('\t欢迎来到王者荣耀')
print('*'*40)

role = input('请选择游戏人物:(1.鲁班 2.后羿 3.李白 4.孙尚香 5.貂蝉 6.诸葛亮)')

coins = 1000

# 保存自己武器容器
weapon_list = [] 

print('欢迎!{1}来到王者荣耀，当前金币是:{0}'.format(coins,role))

while True:
	choice = int(input('\n请选择:\n 1.购买武器\n 2.打仗\n 3.删除武器\n 4.查看武器\n 5.退出游戏\n'))

	if choice==1:
		# 购买武器
		print('欢迎进到武器库:')
		weapons = [['屠龙刀',500],['樱花枪',400],['98k枪',1000],['手榴弹',800],['碧血剑',700],['鹅毛扇',800]]
		for weapon in weapons:
			print(weapon[0],weapon[1],sep='   ')

		# 提示输入要购买武器
		weaponname = input('请输入要购买的武器名称:')
		# 1.原来有没有买过武器，2.输入的武器名是否在武器库
		if weaponname not in weapon_list:
			#  输入的武器名是否在武器库
			for weapon in weapons:
				if weaponname == weapon[0]:
					# 购买武器
					if coins >= weapon[1]:
						# 扣钱购买
						coins-=weapon[1]
						weapon_list.append(weapon[0])  # 添加到你自己的武器库
						print('{}购买武器:{}成功！'.format(role,weaponname))
						break
					else:
						print('金币不足，赶快打仗挣金币！')
						break
			else:
				print('输入武器名称错误！')
		else:
			print('已经拥有此武器！')

	elif choice==2:
		# 打仗 假设你有多个武器
		print('进入战场......')
		if len(weapon_list)>0:
			# 选择武器
			print('{}拥有的武器如下:'.format(role))
			for weapon in weapon_list:
				print(weapon)

			while True:
				weaponname = input('请选择:')
				# 
				if weaponname in weapon_list:
					# 进入战争状态 默认跟张飞

					ran1 = random.randint(1,20)  # 张飞
					ran2 = random.randint(1,20)  # role
					# 随机选择对战人物

					role_list = ['诸葛亮','孙尚香','貂蝉','鲁班','赵云','张飞','曹操','关羽','周瑜','孙悟空','猪八戒','蜘蛛精','蜈蚣精','白骨精','九尾狐','夜华','白浅']

					ran = random.randint(0,len(role_list))

					# 得到对战人物
					pk_role = role_list[ran]

					# 判断人物是不是自己
					if pk_role==role:
						print('不能跟自己对战！重新进入游戏！')
					else:
						print('{} PK {}'.format(role,pk_role))

						if ran1>ran2:
							print('此局对战：{}胜！！！'.format(pk_role))
						elif ran1<ran2:
							
							coins+=200
							print('此局对战:{}胜! 金币:{}'.format(role,coins))
						else:
							print('此局平局,可以再次对战！')

					break
				else:
					print('选择的武器不存在,请重新选择')
		else:
			print('还没有购买武器,赶快使用金币购买武器去吧！')

	elif choice==3:
		# 删除武器
		print('武器太多，很沉,扔几个.....')
		if len(weapon_list)>0:
			print('{}拥有的武器如下:'.format(role))
			for weapon in weapon_list:
				print(weapon)

			while True:		
				weaponname = input('请选择要删除的武器名称:')
				if weaponname in weapon_list:
					# 删除武器  remove(obj)  pop(index)  clear   del weapon_list[index]
					weapon_list.remove(weaponname)
					#思考 
					# print(weapons)
					for weapon in weapons: #  [['98k枪',1000],[],[]]
						if weaponname==weapon[0]:
							coins +=weapon[1]
							break

					break
				else:
					print('武器名称输入有误！')

		else:
			print('你都没有武器，还沉啥呀....,赶快购买去吧！')


	elif choice==4:
		# 遍历武器
		print('{}拥有的武器如下:'.format(role))
		for weapon in weapon_list:
			print(weapon)
		# 查看金币	
		print('总金币:',coins)

	elif choice==5:
		answer = input('确定要离开王者荣耀游戏吗(yes/no)?')
		if answer=='yes':
			print('game over!!!')
			break
	else:
		print('输入错误，请重新选择')