for i in {0..1457}; do
    wget https://copypastas.ru/c/$i.php &
done
for file in *.php; do
    cat $file | jq '.c' | python3 -c 'import codecs;print(" ".join(codecs.escape_decode(input())[0].decode().replace("&&", "")[1:-1].split()))';
done > data2.txt
cat data*.txt | rg -v 'пид(о|а)р|даун' > data
rm *.php data2.txt

