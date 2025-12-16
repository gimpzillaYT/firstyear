#include <iostream>
#include <cmath>
#include <ctime>
#define houseSize 6
using namespace std;
int house[houseSize] = {0, 0, 0, 0, 0, 0};


//prototypes
void fortuneTell();
int rng(int n);
void buildHouse(int n);
void printHouse(int n);
int hexagramNumber();
char *omenWord(int n);
char *hexName(int n);
int hexIndex(int n, int k);

//main
int main(){
    srand(time(NULL));

    char *question[200];
    
fortuneTell();}

//functions
int rng(int n){
return (rand() % n) + 1;}

void fortuneTell(){
/*a playground for new prints, develop features here
and branch them into functions below*/
        buildHouse(houseSize);
        cout << hexName(hexagramNumber()) << endl;

        for(int i = 0; i < houseSize; i++){
        if(house[i] == 6){ cout << house[i] << " in the " << i + 1 << " house; " 
        << omenWord(6) << omenWord(6) << endl;}
        if(house[i] == 9){ cout << house[i] << " in the " << i + 1 << " house; " 
        << omenWord(9) << omenWord(9) << endl;}}
cout << endl;}


void buildHouse(int n){
/* adds rng value 2 or 3 to each index variable, 
simulating real world iChing coin method*/
        int loopCount = 0;
        while(loopCount < 3){ 
                for(int i = 0; i < n; i++){
                house[i] += rng(2) + 1;  
        } loopCount++; }
printHouse(n);}

void printHouse(int n){
        for(int i = n - 1; i >= 0; i--){
        int temp = house[i];    
        if(temp == 6){ cout << "---X---\n";}
        if(temp == 7){ cout << "-------\n";}
        if(temp == 8){ cout << "--   --\n";}
        if(temp == 9){ cout << "---O---\n";}}
cout << endl;}

int hexagramNumber(){
/*tempArray changes the House[] variables to values 1 or 0
comparew arrays, returns int to matching hexIndex number*/   
        int tempHouse [houseSize];
    
        for(int i = 0; i < houseSize; i++){
                if(house[i] == 6 || house[i] == 8){
                tempHouse[i] = false;} 
        else { tempHouse[i] = true; }} 

        int tempHex = 0, k = 0;
        while(k < houseSize){
                if(tempHouse[k] != hexIndex(tempHex, k)){
                tempHex++;
                k = 0;} 
        else { k++; }}
        
return tempHex;}    


char *omenWord(int n){
/*only accepts int 6(bad) or 9(good) else donkey*/
        char *badOmen[10] = {"dark ", "abysmally ", "whole ", "contemplation ", "splitting ",
        "obstruct ", "folly ", "spoils ", "blame ", "further "};
        char *goodOmen[10] = {"joyous ", "perseverent ", "still ", "keeping ", "open ", "gentle ",
        "fire ", "maiden ", "following ", "deliverence "};
if(n == 9){ return goodOmen[rng(10) - 1];}
if(n == 6){ return badOmen[rng(10) - 1];}
return "donkey";}

char *hexName(int n){
        char *hexNames[64] = {"1. Ch'ien\n", "44. Kou\n", "13. T'ung Jen\n", "10. Lu\n", "9. Hsiao Ch'u\n",
         "14. Ta Yu\n", "43. Kaui\n", "33. Tun\n", "25. Wu Wang\n", "61. Chung Fu\n", "26. Ta Ch'u\n",
         "34. Ta Chuang\n", "6. Sung\n", "37. Chia Jen\n", "38. K'uei\n", "5. Hsu\n", "57. Sun\n",
         "30. Li\n", "58. Tui\n", "50. Ting\n", "49. Ko\n", "28. Ta Kuo\n", "12. P'i\n", "42. I\n",
         "41. Sun\n", "11. T'ai\n", "59. Huan\n", "22. Pi\n", "54. Kuei Mei\n", "53. Chien\n",
         "21. Shih Ho\n", "60. Chieh\n", "18. Ku\n", "55. Feng\n", "56. Lu\n", "17. Sui\n", "32. Heng\n",
         "31. Hsien\n", "47. K'un\n", "48. Ching\n", "63. Chi Chi\n", "64. Wei Chi\n", "20. Kuan",
         "27. I\n", "19. Lin\n", "4. Meng\n", "36. Ming I\n", "52. Ken\n", "51. Chen\n", "35. Chin\n",
         "3. Chun\n", "46. Sheng\n", "62. Hsiao Kuo\n", "45. Ts'ui\n", "29. K'an\n", "39. Chien\n",
         "40. Hsieh\n", "24. Fu\n", "7. Shih\n", "15. Ch'ien\n", "16. Yu\n", "8. Pi\n", "23. Po\n", "2. K'un"};
return hexNames[n];}

int hexIndex(int n, int k){
/*index for all 64 hexagrams, catalogged by t/f data
potenitally looking for better way to initialize hex[][] */
    int hex [64][houseSize];
    int ch_ien [houseSize] = {true, true, true, true, true, true};
    for(int i = 0; i < houseSize; i++){
        hex[0][i] = ch_ien[i]; }
    int kou [houseSize] = {false, true, true, true, true, true};
    for(int i = 0; i < houseSize; i++){
        hex[1][i] = kou[i]; }
    int t_ungJen [houseSize] = {true, false, true, true, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[2][i] = t_ungJen[i]; }
    int lu [houseSize] = {true, true, false, true, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[3][i] = lu[i]; }
    int hsiaoCh_u [houseSize] = {true, true, true, false, true, true}; 
    for(int i = 0; i < houseSize; i++){
            hex[4][i] = hsiaoCh_u[i]; }
    int taYu [houseSize] = {true, true, true, true, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[5][i] = taYu[i]; }
    int kuai [houseSize] = {true, true, true, true, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[6][i] = kuai[i]; }
    int tun [houseSize] = {false, false, true, true, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[7][i] = tun[i]; }
    int wuWang [houseSize] = {true, false, false, true, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[8][i] = wuWang[i]; }
    int chungFu [houseSize] = {true, true, false, false, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[9][i] = chungFu[i]; }
    int taCh_u [houseSize] = {true, true, true, false, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[10][i] = taCh_u[i]; }
    int taChuang [houseSize] = {true, true, true, true, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[11][i] = taChuang[i]; }
    int sung [houseSize] = {false, true, false, true, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[12][i] = sung[i]; }
    int chiaJen [houseSize] = {true, false, true, false, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[13][i] = chiaJen[i]; }
    int k_uei [houseSize] = {true, true, false, true, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[14][i] = k_uei[i]; }
    int hsu [houseSize] = {true, true, true, false, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[15][i] = hsu[i]; }
    int sun [houseSize] = {false, true, true, false, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[16][i] = sun[i]; }
    int li [houseSize] = {true, false, true, true, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[17][i] = li[i]; }
    int tui [houseSize] = {true, true, false, true, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[18][i] = tui[i]; }
    int ting [houseSize] = {false, true, true, true, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[19][i] = ting[i]; }
    int ko [houseSize] = {true, false, true, true, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[20][i] = ko[i]; }
    int taKuo [houseSize] = {false, true, true, true, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[21][i] = taKuo[i]; }
    int p_i [houseSize] = {false, false, false, true, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[22][i] = p_i[i]; }
    int i_ [houseSize] = {true, false, false, false, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[23][i] = i_[i]; }
    int sun_ [houseSize] = {true, true, false, false, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[24][i] = sun_[i]; }
    int t_ai [houseSize] = {true, true, true, false, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[25][i] = t_ai[i]; }
    int huan [houseSize] = {false, true, false, false, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[26][i] = huan[i]; }
    int pi [houseSize] = {true, false, true, false, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[27][i] = pi[i]; }
    int kueiMei [houseSize] = {true, true, false, true, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[28][i] = kueiMei[i]; }
    int chien [houseSize] = {false, false, true, false, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[29][i] = chien[i]; }
    int shihHo  [houseSize] = {true, false, false, true, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[30][i] = shihHo[i]; }
    int chieh [houseSize] = {true, true, false, false, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[31][i] = chieh[i]; }
    int ku [houseSize] = {false, true, true, false, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[32][i] = ku[i]; }
    int feng [houseSize] = {true, false, true, true, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[33][i] = feng[i]; }
    int lu_ [houseSize] = {false, false, true, true, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[34][i] = lu_[i]; }
    int sui [houseSize] = {true, false, false, true, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[35][i] = sui[i]; }
    int heng [houseSize] = {false, true, true, true, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[36][i] = heng[i]; }
    int hsien [houseSize] = {false, false, true, true, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[37][i] = hsien[i]; }
    int k_un [houseSize] = {false, true, false, true, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[38][i] = k_un[i]; }
    int ching [houseSize] = {false, true, true, false, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[39][i] = ching[i]; }
    int chiChi [houseSize] = {true, false, true, false, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[40][i] = chiChi[i]; }
    int weiChi [houseSize] = {false, true, false, true, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[41][i] = weiChi[i]; }
    int kuan [houseSize] = {false, false, false, false, true, true};
    for(int i = 0; i < houseSize; i++){
            hex[42][i] = kuan[i]; }
    int i_i [houseSize] = {true, false, false, false, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[43][i] = i_i[i]; }
    int lin [houseSize] = {true, true, false, false, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[44][i] = lin[i]; }
    int meng [houseSize] = {false, true, false, false, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[45][i] = meng[i]; }
    int mingI [houseSize] = {true, false, true, false, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[46][i] = mingI[i]; }
    int ken [houseSize] = {false, false, true, false, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[47][i] = ken[i]; }
    int chen [houseSize] = {true, false, false, true, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[48][i] = chen[i]; }
    int chin [houseSize] = {false, false, false, true, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[49][i] = chin[i]; }
    int chun [houseSize] = {true, false, false, false, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[50][i] = chun[i]; }
    int sheng [houseSize] = {false, true, true, false, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[51][i] = sheng[i]; }
    int hsiaoKuo [houseSize] = {false, false, true, true, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[52][i] = hsiaoKuo[i]; }
    int ts_ui [houseSize] = {false, false, false, true, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[53][i] = ts_ui[i]; }
    int k_an [houseSize] = {false, true, false, false, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[54][i] = k_an[i]; }
    int chien_ [houseSize] = {false, false, true, false, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[55][i] = chien_[i]; }
    int hsieh [houseSize] = {false, true, false, true, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[56][i] = hsieh[i]; }
    int fu [houseSize] = {true, false, false, false, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[57][i] = fu[i]; }
    int shih [houseSize] = {false, true, false, false, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[58][i] = shih[i]; }
    int ch_ien_ [houseSize] = {false, false, true, false, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[59][i] = ch_ien_[i]; }
    int yu [houseSize] = {false, false, false, true, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[60][i] = yu[i]; }
    int pi_ [houseSize] = {false, false, false, false, true, false};
    for(int i = 0; i < houseSize; i++){
            hex[61][i] = pi_[i]; }
    int po [houseSize] = {false, false, false, false, false, true};
    for(int i = 0; i < houseSize; i++){
            hex[62][i] = po[i]; }
    int k_un_ [houseSize] = {false, false, false, false, false, false};
    for(int i = 0; i < houseSize; i++){
            hex[63][i] = k_un_[i]; }

return hex[n][k];}

