import pandas as pd
import re


input_file_name = "/home/cair/Desktop/data/datasets(translated)/india+china+pakistan(final dataset).csv"
output_file_name = "final_output_entities.csv"

df = pd.read_csv(input_file_name)

MAX_VALUE = df.shape[0]
print(MAX_VALUE)

class results():
	
	# def try_detect(cell):
	# 	try:
	# 		detected_lang = detect(cell)
	# 	except:
	# 		detected_lang = None
	# 	return detected_lang

	def random_results(file_name, no_of_rows):

		df_elements = df.sample(n=no_of_rows)
		return df_elements
		
	def distilled_results(file_name, no_of_rows):


		#'zh_translate_tool1'
		df_extract_list = df['zh_translate_tool1'].str.findall('[\u4e00-\u9fff]+')
		df_list = list()
		# print(df_extract_list)
		for a in df_extract_list:
			if isinstance(a,list) == True:
				if len(a) != 0:
					df_list.append(str(a[0]))
	
		#print(df_list)
		
		df_distill = df[df['zh_translate_tool1'].isin(df_list)] 
		df_distill = df_distill.sample(n=no_of_rows)
		return df_distill
	
	
if __name__ == "__main__":

	while True:
	
		row_range = int(input(f"enter the desired number of rows. \n your max limit is {MAX_VALUE}\n"))
		
		if row_range > MAX_VALUE:
			print("row range exceeded limit. Please try again\n")
			continue
		
		else:
			choice = int(input(f"enter your choice\n1. randomly select any {row_range} number of rows.\n2. select {row_range} rows with proper translated output.\n"))
			
			if choice == 1:
			
				df_result = results.random_results(input_file_name, row_range)
				print(df_result.head())
				break
				
			elif choice == 2:
			
				df_result = results.distilled_results(input_file_name, row_range)
				df_result = df_result.drop('Unnamed: 0',axis=1)
				print(df_result.columns)
				break
				
			else:
				print("please enter right choice\n")
				continue
		
	ch = input("do you want to save the output (y/n)?\n")
	if ch=='y':
		df_result.to_csv(output_file_name)
		print(f"output saved as {output_file_name}")
	
		
			
	
	
