base_path=../../data
rm -rf $base_path
for dataset in foo bar; do
    for y in 2014 2015; do
        for m in $(seq -w 1 12); do
            days=30
            if [ $m -eq 2 ]; then
                days=28
            elif [[ "1 3 5 7 8 10 12" =~ $m ]]; then
                days=31
            fi
            for d in $(seq -w 1 $days); do
                for h in $(seq -w 0 23); do
                    dir=$base_path/$dataset/$y/$m/$d/$h
                    echo $dir
                    mkdir -pv $dir
                    touch $dir/${dataset}{1,2,3}
                done
            done
        done
    done
done
