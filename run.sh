function run_data() {
    local name=$1

    local input="data/$name.in.txt"
    local output="output/$name.out.txt"

    echo "$name"
    $(./oskour.py $input > $output)
}

run_data a_an_example
run_data b_better_start_small
run_data c_collaboration
run_data d_dense_schedule
run_data e_exceptional_skills
run_data f_find_great_mentors