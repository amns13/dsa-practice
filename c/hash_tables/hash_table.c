#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

const int _table_size  = 20;
const char *_empty_slot_placeholder = "";

typedef struct key_value {
    char *key;
    char *value;
} key_value;

typedef struct hash_table {
    int size;
    key_value **data;
} hash_table;

int hash(char *key, int m) {
    int hash_value = 0;
    for (int i = 0; key[i] != '\0'; ++i) {
        hash_value = ((hash_value * 31) % m + (key[i]) % m) % m;
    }

    return hash_value % m;
}

void check_address(void *ptr) {
    if (!ptr) {
        exit(EXIT_FAILURE);
    }
}

bool is_key_valid(const char *key) {
    return strcmp(key, _empty_slot_placeholder) != 0;
}

key_value *create_key_value_pair(char *key, char* value) {
    key_value *kv = malloc(sizeof(key_value));
    check_address(kv);
    kv->key = key;
    kv->value = value;
    return kv;
}

hash_table *create_hash_table() {
    hash_table *ht = malloc(sizeof(hash_table));
    check_address(ht);
    ht->size = _table_size;
    key_value **kv = malloc(sizeof(key_value*) * _table_size);
    check_address(kv);
    for (int i = 0; i < _table_size; ++i) {
        kv[i] = NULL;
    }
    ht->data = kv;

    return ht;
}

int _get_key_location(hash_table *ht, char *key) {
    if (is_key_valid(key)) {
        int index = hash(key, ht->size);
        int original_index = index;

        while (ht->data[index]) {
            if (strcmp(ht->data[index]->key, key) == 0) {
                return index;
            }
            index = (index + 1) % ht->size;
            if (index == original_index) {
                break;
            }
        }
    }
    return -1;
}

char *get(hash_table *ht, char *key) {
    int index = _get_key_location(ht, key);
    return index == -1 ? NULL : ht->data[index]->value;
}

bool set(hash_table *ht, char *key, char *value) {
    if (!is_key_valid(key)) {
        return false;
    }

    int index = _get_key_location(ht, key);
    if (index == -1) {
        index = hash(key, ht->size);
        int original_index = index;
        printf("Original Index for %s: %d\n", key, index);

        while (ht->data[index] && is_key_valid(ht->data[index]->key)) {
            index = (index + 1) % ht->size;
            if (index == original_index) {
                printf("Table is full\n");
                return false;
            }
        }
        key_value *kv = create_key_value_pair(key, value);
        // TODO: in case if deleted entry is present here, then it should be freed first
        ht->data[index] = kv;
    } else {
        ht->data[index]->value = value;
    }

    return true;

}

bool delete(hash_table *ht, char *key) {
    if (!is_key_valid(key)) {
        return false;
    }

    int index = _get_key_location(ht, key);
    if (index == -1) {
        return false;
    }

    ht->data[index]->key = _empty_slot_placeholder;
    ht->data[index]->value = _empty_slot_placeholder;
    return true;
}

void print_hash_table(hash_table *ht) {
    printf("\n********************\n");
    for (int i = 0; i < ht->size; ++i) {
        printf("%2d: ", i);
        if (ht->data[i]) {
            if (is_key_valid(ht->data[i]->key)) {
                printf("%s -> %s\n", ht->data[i]->key, ht->data[i]->value);
            } else {
                printf("Deleted entry.\n");
            }
        } else {
            printf("\n");
        }
    }
    printf("\n********************\n");
}

int main(void) {
    hash_table *ht = create_hash_table();
    set(ht, "abhishek", "CS1");
    set(ht, "alankar", "CS2");
    set(ht, "aman", "CS3");
    set(ht, "ravi ranjan", "CS26");
    set(ht, "ashutosh", "cs50");
    set(ht, "atish", "EEE1");
    set(ht, "ravi kumar", "EEE2");
    set(ht, "saurav", "EEE3");
    set(ht, "prabhash", "RPS001");
    set(ht, "abhishek og", "RPS002");
    set(ht, "sudhanshu", "RPS003");
    set(ht, "ashish", "IPS1");
    set(ht, "rohit", "rnc1");
    set(ht, "subham soni", "rnc2");
    set(ht, "kundan", "rnc3");
    set(ht, "dummy", "dummy1");
    print_hash_table(ht);

    printf("abhishek -> %s\n", get(ht, "abhishek"));
    printf("rohit -> %s\n", get(ht, "rohit"));

    delete(ht, "ashish");
    printf("ashish -> %s\n", get(ht, "ashish"));
    delete(ht, "aman");
    set(ht, "rohit", "rnc_bhai");
    set(ht, "dummy", "dummy1");
    print_hash_table(ht);
    set(ht, "aman", "ME");
    print_hash_table(ht);

    return 0;
}
