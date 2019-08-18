
file_to_read = open("listsIdenticalObjsFormated.txt", "r")
file_to_write = open("Counted_apps_per_line.csv", "w")
line_counter = 0
for line in file_to_read:
	line_counter += 1
	count = line.count(",")
	content_to_write = str(line_counter)+","+str(count + 1)+"\n"
	file_to_write.write(content_to_write)
# print(line_counter,",",+(count  + 1))
file_to_read.close()
file_to_write.close()
