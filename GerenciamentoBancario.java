package com.mycompany.gerenciamentobancario;

import java.util.Scanner;
/**
 *
 * @author bryan
 */
public class GerenciamentoBancario {
    
    long cpf;
    double saldo = 0;
    String nome;
    String sobrenome;
    
    Scanner scan = new Scanner(System.in);
    /*ver saldo*/
    public void cons_saldo(){
        System.out.println(nome +" "+ sobrenome);
        System.out.println(cpf);
        System.out.println("seu saldo é" + saldo);       
    }
    
    /*depositar dinheiro*/
    public void depositar(){
        double valor_dep = 0;
        System.out.println("Quanto você deseja depositar?");
        valor_dep = scan.nextDouble();
            if (valor_dep <= 0 ){
                System.out.println("Valor invalido!");
            }
            else{    
                saldo = valor_dep + saldo;
                System.out.printf("Você depositou: %.2f\n", valor_dep);
            }
    }
    
    /*sacar dinheiro*/
    public void sacar(){
        double valor_sac = 0;
        System.out.println("\nQuanto voce quer sacar:");
        valor_sac = scan.nextDouble();
        if(valor_sac > saldo ){
            System.out.println("Valor invalido!");
        }
        else{
        saldo = saldo - valor_sac;
        System.out.printf("\nvoce sacou: %.2f",valor_sac);
        }
    }
    
    /*cadastrar*/
    public void cadastrar(){
        System.out.println("\nOla, qual e o seu primeiro nome?");
        nome = scan.next();
        System.out.println("\nqual seu sobrenome");
        sobrenome = scan.next();
        System.out.println("\nqual seu cpf");
        cpf = scan.nextLong();
        System.out.println("\nOla," + sobrenome + "prazer em conhecelo!");
    }
    /*rodar progmama*/
    public static void main(String[] args){
        GerenciamentoBancario cliente = new GerenciamentoBancario();
        
        Scanner scan = new Scanner(System.in);
        
        cliente.cadastrar();
        
        String continuar = "Sim";        
        while (!continuar.equals("Nao")){
            
            System.out.println("\n----------------");
            System.out.println("\n     Conta");
            System.out.println("\n----------------");
            
            System.out.println("\nEscolha uma opçao:");
            System.out.println("\n1. Sacar");
            System.out.println("\n2. Depositar");
            System.out.println("\n3. Consultar saldo");
            int opção = scan.nextInt();
            
            if (opção == 1){
                cliente.sacar();
            }
            else if (opção== 2){
                cliente.depositar();
            }
            else if (opção == 3){
                cliente.cons_saldo();
            }
            else{
                System.out.println("\nOpcao invalida!");
            }                    
            System.out.println("\nVoce gostaria de continuar: Sim | Nao");              
            continuar = scan.next();                    
        }
        scan.close();
    }
}
