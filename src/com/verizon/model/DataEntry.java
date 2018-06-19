package com.verizon.model;

public class DataEntry {
	private String zipcode;
	private Double age;
	private String race;
	private Double income;
	private Integer population;
	
	public DataEntry(String zipcode, Double age, String race, Double income, Integer population) {
		this.zipcode = zipcode;
		this.age = age;
		this.race = race;
		this.income = income;
		this.population = population;
	}

	public String getZipcode() {
		return zipcode;
	}

	public void setZipcode(String zipcode) {
		this.zipcode = zipcode;
	}

	public Double getAge() {
		return age;
	}

	public void setAge(Double age) {
		this.age = age;
	}

	public String getRace() {
		return race;
	}

	public void setRace(String race) {
		this.race = race;
	}

	public Double getIncome() {
		return income;
	}

	public void setIncome(Double income) {
		this.income = income;
	}

	public Integer getPopulation() {
		return population;
	}

	public void setPopulation(Integer population) {
		this.population = population;
	}
	
	

}
