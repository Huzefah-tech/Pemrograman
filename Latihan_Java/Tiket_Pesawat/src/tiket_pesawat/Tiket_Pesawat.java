package tiket_pesawat;
import java.util.Scanner;
public class Tiket_Pesawat {
public static void main(String[] args) {
Scanner input=new Scanner (System.in);
int pil=0;
int hargaD,hargaA,tiketD,tiketA,metode;
int hargatot=0,uang=0, kembali=0;
double pajak=0;
System.out.println(" PEMESANAN TIKET PESAWAT ");
System.out.println("==============================");
System.out.println();
System.out.print("Masukan Nama Anda : ");
String nama = input.next();
String pesawat[][] = {{"", "Pesawat Elang", "Pesawat SSinga", "Pesawat RJK "},
{"", "3245", "3500", "4231", }};
System.out.println("Jenis pesawat code pesawat");
int var1 = 0;
int var2 = 1;
//menampilkan jenis pesawat
for (int i = 1; i < pesawat[var1].length; i++){
System.out.println(i + "."+ pesawat[var1][i]+ " "+ pesawat [var2][i]);
}
System.out.print("Masukan Pilihan : ");
int kode = input.nextInt();
System.out.println("Daftar Tiket - Harga");
System.out.println("--------------------------------------------------------------------------");
System.out.println("| No| Asal | Tujuan | Harga Tiket Dewasa | Harga Tiket Anak |");
System.out.println("--------------------------------------------------------------------------");
System.out.println("| 1 |Palembang |Jakarta | Rp.750.000 | Rp.700.000 |");
System.out.println("| 2 |Jakarta |Denpasar-Bali | Rp.995.000 | Rp.800.000 |");
System.out.println("| 3 |Denpasar-bali|Surabaya | Rp.700.000 | Rp.650.000 |");
System.out.println("| 4 |Surabaya |Medan | Rp.2.750.000 | Rp.2.600.000 |");
System.out.println("--------------------------------------------------------------------------");
System.out.println("--------------------------------------------------------------------------");
System.out.print("Masukan Nomor Pilihan = ");
pil = input.nextInt();
switch (pil){
case 1:
System.out.print("Masukan Jumlah Tiket Dewasa : ");
hargaD=input.nextInt();
tiketD=hargaD*750000;
System.out.print("Masukan Jumlah Tiket Anak-anak : ");
hargaA=input.nextInt();
tiketA=hargaA*700000;
hargatot=tiketD+tiketA;
System.out.println("Harga Sebelum Pajak= "+hargatot);
if(hargatot>=0){
pajak=hargatot*0.05;
System.out.println("Pajak = Rp."+pajak+",-");
hargatot = (int) (hargatot+pajak);
System.out.println("Total harga = Rp."+hargatot+",-");
System.out.println("Sudah Termasuk Pajak 5%");
}
System.out.println("----------------------");
System.out.println("Metode Pembayaran");
System.out.println("1.Transfer");
System.out.println("2.Internet Banking");
System.out.println("----------------------");
System.out.print("Masukan Pilihan Metode Pembayaran = ");
metode = input.nextInt();
if(metode==1){
System.out.println("Transfer");
}
else if(metode==2){
System.out.println("Internet Banking");
}
else{
System.out.println("Salah Input");
}
System.out.print("Masukan Uang yang diberikan Rp.");
uang = input.nextInt();
while(uang<hargatot){
System.out.println("Uang yg anda masukan kurang Masukan Uang Kembali: ");
System.out.println("Masukkan uang Kembali...");
int tk=input.nextInt();
uang=uang+tk;
}
kembali=(uang-hargatot);

System.out.println("================================");
System.out.println(" DETAIL PEMESANAN ");
System.out.println("================================");
System.out.println("Nama = "+nama);
System.out.println("Asal = Palembang");
System.out.println("Tujuan = Jakarta");
System.out.println("Tiket Dewasa = "+hargaD);
System.out.println("Tiket Anak-anak = "+hargaA);
System.out.println("Total Harga Tiket = "+hargatot);
System.out.println("Pembayaran = "+uang);
System.out.println("Kembalian Anda = Rp."+kembali);
System.out.println("code boking(PNR) =df23150");
System.out.println("================================");
System.out.println("TerimaKasih Atas Pemesanan Anda");
System.out.println("================================");
break;
case 2:
System.out.print("Masukan Jumlah Tiket Dewasa : ");
hargaD=input.nextInt();
tiketD=hargaD*995000;
System.out.print("Masukan Jumlah Tiket Anak-anak : ");
hargaA=input.nextInt();
tiketA=hargaA*800000;
hargatot=tiketD+tiketA;
System.out.println("================================");
System.out.println("Harga Sebelum Pajak:"+hargatot);
if(hargatot>=0){
pajak=hargatot*0.05;
System.out.println("Pajak = Rp."+pajak+",-");
hargatot = (int) (hargatot+pajak);
System.out.println("Total harga = Rp."+hargatot+",-");
System.out.println("Sudah Termasuk Pajak 5%");
}
System.out.println("----------------------");
System.out.println("Metode Pembayaran");
System.out.println("1.Transfer");
System.out.println("2.Internet Banking");
System.out.println("----------------------");
System.out.print("Masukan Pilihan Metode Pembayaran = ");
metode = input.nextInt();
if(metode==1){
System.out.println("Transfer");
}
else if(metode==2){
System.out.println("Internet Banking");
}
else{
System.out.println("Salah Input");
}
System.out.print("Masukan Uang yang diberikan Rp.");
uang = input.nextInt();
while(uang<hargatot){
System.out.println("Uang yg anda masukan kurang Masukan Uang Kembali: ");
System.out.println("Masukkan uang Kembali...");
int tk=input.nextInt();
uang=uang+tk;
}
kembali=(uang-hargatot);
System.out.println("================================");
System.out.println(" DETAIL PEMESANAN ");
System.out.println("================================");
System.out.println("Nama = "+nama);
System.out.println("Asal = Jakarta");
System.out.println("Tujuan = Denpasar-Bali");
System.out.println("Tiket Dewasa = "+hargaD);
System.out.println("Tiket Anak-anak = "+hargaA);
System.out.println("Total Harga Tiket = "+hargatot);
System.out.println("Pembayaran = "+uang);
System.out.println("Kembalian Anda = Rp."+kembali);
System.out.println("code boking(PNR) =rd34290");
System.out.println("================================");
System.out.println("TerimaKasih Atas Pemesanan Anda");
System.out.println("================================");
break;
case 3:
System.out.print("Masukan Jumlah Tiket Dewasa : ");
hargaD=input.nextInt();
tiketD=hargaD*700000;
System.out.print("Masukan Jumlah Tiket Anak-anak : ");
hargaA=input.nextInt();
tiketA=hargaA*650000;
hargatot=tiketD+tiketA;
System.out.println("================================");
System.out.println("Harga Sebelum Pajak:"+hargatot);
if(hargatot>=0){
pajak=hargatot*0.05;
System.out.println("Pajak = Rp."+pajak+",-");
hargatot = (int) (hargatot+pajak);
System.out.println("Total harga = Rp."+hargatot+",-");
System.out.println("Sudah Termasuk Pajak 5%");
}
System.out.println("----------------------");
System.out.println("Metode Pembayaran");
System.out.println("1.Transfer");
System.out.println("2.Internet Banking");
System.out.println("----------------------");
System.out.print("Masukan Pilihan Metode Pembayaran = ");
metode = input.nextInt();
if(metode==1){
System.out.println("Transfer");
}
else if(metode==2){
System.out.println("Internet Banking");
}
else{
System.out.println("Salah Input");
}
System.out.print("Masukan Uang yang diberikan Rp.");
uang = input.nextInt();
while(uang<hargatot){
System.out.println("Uang yg anda masukan kurang Masukan Uang Kembali: ");
System.out.println("Masukkan uang Kembali...");
int tk=input.nextInt();
uang=uang+tk;
}
kembali=(uang-hargatot);
System.out.println("================================");
System.out.println(" DETAIL PEMESANAN ");
System.out.println("================================");
System.out.println("Nama = "+nama);
System.out.println("Asal = Denpasar-Bali");
System.out.println("Tujuan = Surabaya");
System.out.println("Tiket Dewasa = "+hargaD);
System.out.println("Tiket Anak-anak = "+hargaA);
System.out.println("Total Harga Tiket = "+hargatot);
System.out.println("Pembayaran = "+uang);
System.out.println("Kembalian Anda = Rp."+kembali);
System.out.println("code boking(PNR) =sa65540");
System.out.println("================================");
System.out.println("TerimaKasih Atas Pemesanan Anda");
System.out.println("================================");
break;
case 4:
System.out.print("Masukan Jumlah Tiket Dewasa : ");
hargaD=input.nextInt();
tiketD=hargaD*2750000;
System.out.print("Masukan Jumlah Tiket Anak-anak : ");
hargaA=input.nextInt();
tiketA=hargaA*2600000;
hargatot=tiketD+tiketA;
System.out.println("================================");
System.out.println("Harga Sebelum Pajak:"+hargatot);
if(hargatot>=0){
pajak=hargatot*0.05;
System.out.println("Pajak = Rp."+pajak+",-");
hargatot = (int) (hargatot+pajak);
System.out.println("Total harga = Rp."+hargatot+",-");
System.out.println("Sudah Termasuk Pajak 5%");
}
System.out.println("----------------------");
System.out.println("Metode Pembayaran");
System.out.println("1.Transfer");
System.out.println("2.Internet Banking");
System.out.println("----------------------");
System.out.print("Masukan Pilihan Metode Pembayaran = ");
metode = input.nextInt();
if(metode==1){
System.out.println("Transfer");
}
else if(metode==2){
System.out.println("Internet Banking");
}
else{
System.out.println("Salah Input");
}
System.out.print("Masukan Uang yang diberikan Rp.");
uang = input.nextInt();
while(uang<hargatot){
System.out.println("Uang yg anda masukan kurang Masukan Uang Kembali: ");
System.out.println("Masukkan uang Kembali...");
int tk=input.nextInt();
uang=uang+tk;
}
kembali=(uang-hargatot);
System.out.println("================================");
System.out.println(" DETAIL PEMESANAN ");
System.out.println("================================");
System.out.println("Nama = "+nama);
System.out.println("Asal = Surabaya");
System.out.println("Tujuan = Medan");
System.out.println("Tiket Dewasa = "+hargaD);
System.out.println("Tiket Anak-anak = "+hargaA);
System.out.println("Total Harga Tiket = "+hargatot);
System.out.println("Pembayaran = "+uang);
System.out.println("Kembalian Anda = Rp."+kembali);
System.out.println("code boking(PNR) =ye21389");
System.out.println("================================");
System.out.println("TerimaKasih Atas Pemesanan Anda");
System.out.println("================================");
break;
default:
System.out.println("Salah Input");
break;
}
}
}
