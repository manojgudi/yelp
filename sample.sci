
// Functions for qualitative feature extraction

//## Sample 
//line
//to be
//commented ##

//## another sample
//line to be commented ##

exec   sample_header2.sci
exec abc.sce
  exec   some_folder/yass.sci
exec sample_header.sci
exec sample.sci

// function [NOO] = vector(something)

// exec this_wont_be_expanded.sci

// Some random pre-existsing comments
// functions

function  [output1, output3] = sample_function(inputargs)
endfunction

 function [output2] = sample_function2(inputargs)
 
function [sum_vector, variable_with_no_return_assigned] = vector_sum(image_mat, mode_str)
	
	image_mat_size = size(image_mat);

	select mode_str

	case "cols" then // Sum of each column
		cols_sum = []
		for i = 1 : image_mat_size(2)
			col_sum(1,$+1) = sum(image_mat(:,i)); // col_sum is row vector
		end
		sum_vector = col_sum;
		col_sum = [];

	case "rows" then // Sum of each row
		row_sum = []
		for i = 1 : image_mat_size(1)
			row_sum(1,$+1) = sum(image_mat(i,:)); // row_sum is row vector
		end
		sum_vector = row_sum;
		row_sum = [];

	else
		printf("check for args");
	end

endfunction
